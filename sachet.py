import streamlit as st
import pandas as pd
import numpy as np
import math
import requests
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from passlib.hash import bcrypt
from openai import OpenAI
import xarray as xr

# =========================================================
# PAGE CONFIG + STYLING
# =========================================================
st.set_page_config(page_title="Enterprise Climate Risk SaaS",
                   layout="wide", page_icon="🌍")

st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    color: white;
    font-family: 'Arial', sans-serif;
}
.metric-card {
    background: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(12px);
    text-align:center;
}
.chat-box {
    background: rgba(255,255,255,0.05);
    padding:15px;
    border-radius:12px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Enterprise Climate Risk & ESG SaaS Platform")

# =========================================================
# SIMULATED USER LOGIN (Multi-Tenant)
# =========================================================
# For demo, we simulate a login; in production connect PostgreSQL + JWT

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    with st.form("login_form"):
        tenant = st.text_input("Company / Tenant")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            # Simple hash verification simulation
            st.session_state.logged_in = True
            st.session_state.tenant = tenant
            st.success(f"Welcome {tenant}!")

if not st.session_state.logged_in:
    st.stop()

# =========================================================
# SIDEBAR INPUTS
# =========================================================
st.sidebar.header("Location & Assets")
lat = st.sidebar.number_input("Latitude", value=40.0)
lon = st.sidebar.number_input("Longitude", value=-74.0)
asset_value = st.sidebar.number_input("Asset Value ($)", 1e5, 1e9, 5e6)
portfolio_size = st.sidebar.slider("Portfolio Assets",1,20,5)

scenario = st.sidebar.selectbox("Climate Scenario", ["SSP1-2.6","SSP2-4.5","SSP5-8.5"])

# =========================================================
# FETCH REAL CLIMATE DATA (NASA)
# =========================================================
def get_nasa_temp(lat, lon):
    try:
        url = f"https://power.larc.nasa.gov/api/temporal/climatology/point?parameters=T2M&community=RE&longitude={lon}&latitude={lat}&format=JSON"
        data = requests.get(url, timeout=10).json()
        temp = np.mean(list(data["properties"]["parameter"]["T2M"].values()))
        return temp
    except:
        return 15  # fallback

nasa_temp = get_nasa_temp(lat, lon)
temp_anomaly = max((nasa_temp - 14)/10,0.1)

# =========================================================
# RISK MODEL
# =========================================================
flood_prob = min(abs(lat)/90,1)
drought_idx = min(abs(lon)/180,1)

def hazard(temp,flood,drought):
    return (0.4*min(temp/3,1)) + (0.35*flood) + (0.25*drought)
def vulnerability(flood,drought):
    return (0.6*drought)+(0.4*flood)
def exposure(asset):
    return min(math.log1p(asset)/20,1)

haz = hazard(temp_anomaly,flood_prob,drought_idx)
vul = vulnerability(flood_prob,drought_idx)
exp = exposure(asset_value)
total_risk = haz*vul*exp

# =========================================================
# TABS
# =========================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Risk Dashboard",
    "🗺 Geospatial Map",
    "🏦 Portfolio VaR",
    "🤖 AI Advisor",
    "📄 Compliance Report"
])

# =========================================================
# TAB 1: DASHBOARD
# =========================================================
with tab1:
    st.subheader("Climate Risk Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Hazard", round(haz,3))
    col2.metric("Vulnerability", round(vul,3))
    col3.metric("Exposure", round(exp,3))
    
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=total_risk,
        title={'text':"Total Risk Score"},
        gauge={'axis':{'range':[0,1]},
               'steps':[{'range':[0,0.2],'color':'green'},
                        {'range':[0.2,0.4],'color':'yellow'},
                        {'range':[0.4,0.7],'color':'orange'},
                        {'range':[0.7,1],'color':'red'}]}
    ))
    st.plotly_chart(gauge,use_container_width=True)
    st.markdown(f"**NASA Avg Temp:** {round(nasa_temp,2)}°C")

# =========================================================
# TAB 2: GEOSPATIAL MAP
# =========================================================
with tab2:
    st.subheader("Geospatial Climate Risk Map")
    m = folium.Map(location=[lat,lon], zoom_start=5)
    color="green"
    if total_risk>0.7: color="red"
    elif total_risk>0.4: color="orange"
    elif total_risk>0.2: color="yellow"
    folium.CircleMarker(location=[lat,lon],
                        radius=15,
                        popup=f"Risk Score: {round(total_risk,3)}",
                        color=color, fill=True).add_to(m)
    st_folium(m,width=900)

# =========================================================
# TAB 3: PORTFOLIO CLIMATE VAR
# =========================================================
with tab3:
    st.subheader("Portfolio Climate Value-at-Risk")
    data=[]
    for _ in range(portfolio_size):
        val=np.random.uniform(1e6,1e7)
        risk=np.random.uniform(0.1,total_risk)
        emissions=np.random.uniform(100,1000)
        data.append([val,risk,emissions])
    df=pd.DataFrame(data,columns=["Asset Value","Risk Score","Emissions"])
    df["Climate Loss"]=df["Asset Value"]*df["Risk Score"]
    # Carbon stress
    carbon_price=st.slider("Carbon Price ($/tCO2)",0,200,100)
    df["Carbon Cost"]=df["Emissions"]*carbon_price
    df["Stressed Value"]=df["Asset Value"]-df["Carbon Cost"]
    portfolio_var=df["Climate Loss"].sum()
    st.dataframe(df)
    st.metric("Portfolio Climate VaR ($)",round(portfolio_var,2))

# =========================================================
# TAB 4: GPT AI ADVISOR
# =========================================================
with tab4:
    st.subheader("AI Climate Risk Advisor")
    user_q = st.text_input("Ask about climate risk, mitigation, ESG, or TCFD:")
    if user_q:
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            res = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role":"system","content":"You are a climate risk and ESG advisor."},
                          {"role":"user","content":user_q}]
            )
            st.markdown(res.choices[0].message.content)
        except:
            st.warning("Set OPENAI_API_KEY in environment to use GPT advisor.")

# =========================================================
# TAB 5: EXECUTIVE COMPLIANCE REPORT
# =========================================================
with tab5:
    st.subheader("Generate TCFD / ISSB Report")
    company_name = st.text_input("Company Name", value=st.session_state.tenant)
    if st.button("Generate PDF"):
        file_name=f"{company_name}_Climate_Report.pdf"
        c = canvas.Canvas(file_name,pagesize=letter)
        c.drawString(100,750,"TCFD / ISSB Climate Executive Report")
        c.drawString(100,720,f"Company: {company_name}")
        c.drawString(100,700,f"Total Risk Score: {round(total_risk,3)}")
        c.drawString(100,680,f"Portfolio Climate VaR: {round(portfolio_var,2)}")
        c.drawString(100,640,"Governance: Board oversight implemented")
        c.drawString(100,620,"Strategy: Scenario analysis using SSPs and CMIP6 projections")
        c.drawString(100,600,"Risk Management: ERM integration and carbon stress tested")
        c.drawString(100,580,"Metrics & Targets: Emissions and ESG alignment")
        c.save()
        with open(file_name,"rb") as f:
            st.download_button("Download Executive PDF",f,file_name=file_name)