import streamlit as st
import time
import json
import os
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai"]["YOUR_API_KEY_HERE"])

st.set_page_config(page_title="Football Quiz GOD MODE", layout="wide")

# ------------------- STYLE -------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#000428,#004e92);
}
.card {
    background: rgba(0,0,0,0.75);
    padding: 25px;
    border-radius: 20px;
    margin-bottom: 20px;
}
button {
    width: 100%;
    height: 50px;
    border-radius: 12px !important;
    background: linear-gradient(45deg,#ff9966,#ff5e62);
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>👑 FOOTBALL QUIZ GOD MODE</h1>", unsafe_allow_html=True)

# ------------------- LEADERBOARD -------------------
FILE = "leaderboard.json"

def load_lb():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_lb(name, score):
    data = load_lb()
    data.append({"name": name, "score": score})
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------- AI QUESTION -------------------
@st.cache_data(ttl=30)
def generate_ai_question(level=1):
    try:
        prompt = f"""
        Generate a football (soccer) trivia question.

        Difficulty: {level}/10
        Must be factual.

        Return JSON:
        {{
            "question": "...",
            "options": ["A","B","C","D"],
            "answer": "..."
        }}
        """

        res = client.chat.completions.create(
            model="gpt-5.3",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.6
        )

        data = json.loads(res.choices[0].message.content)

        return {
            "q": data["question"],
            "options": data["options"],
            "ans": data["answer"]
        }

    except:
        return {
            "q": "Who won the 2022 FIFA World Cup?",
            "options": ["Argentina","France","Brazil","Germany"],
            "ans": "Argentina"
        }

# ------------------- SESSION -------------------
defaults = {
    "started": False,
    "score": 0,
    "lives": 3,
    "streak": 0,
    "xp": 0,
    "level": 1,
    "coins": 0,
    "answered": False,
    "q": None,
    "time": time.time()
}

for k,v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ------------------- SIDEBAR -------------------
with st.sidebar:
    st.markdown("## 🎮 HUD")
    st.metric("🏆 Score", st.session_state.score)
    st.metric("🔥 Streak", st.session_state.streak)
    st.metric("❤️ Lives", st.session_state.lives)
    st.metric("⭐ Level", st.session_state.level)
    st.metric("🪙 Coins", st.session_state.coins)

    st.markdown("## 🛒 Shop")
    if st.button("❤️ Buy Life (10 coins)"):
        if st.session_state.coins >= 10:
            st.session_state.coins -= 10
            st.session_state.lives += 1
            st.success("Life added!")
        else:
            st.error("Not enough coins")

    st.markdown("## 🌍 Leaderboard")
    lb = load_lb()
    for i, p in enumerate(lb):
        st.write(f"{i+1}. {p['name']} - {p['score']}")

# ------------------- START -------------------
if not st.session_state.started:
    if st.button("🚀 START GAME"):
        st.session_state.started = True
        st.session_state.q = generate_ai_question()
        st.session_state.time = time.time()

# ------------------- GAME -------------------
elif st.session_state.lives > 0:

    q = st.session_state.q

    limit = max(5, 10 - st.session_state.level)
    elapsed = int(time.time() - st.session_state.time)
    remaining = max(limit - elapsed, 0)

    st.markdown(f"<h3 style='color:white;'>⏱ {remaining}s</h3>", unsafe_allow_html=True)

    if remaining == 0:
        st.warning("⏰ Time's up!")
        st.session_state.lives -= 1
        st.session_state.q = generate_ai_question(st.session_state.level)
        st.session_state.time = time.time()
        st.rerun()

    st.markdown(f"""
    <div class='card'>
    <h2 style='color:#00ffcc;'>Question</h2>
    <h3 style='color:white;'>{q['q']}</h3>
    </div>
    """, unsafe_allow_html=True)

    for opt in q["options"]:
        if st.button(opt, disabled=st.session_state.answered):
            st.session_state.answered = True

            if opt == q["ans"]:
                st.success("✅ Correct!")
                st.session_state.score += 1
                st.session_state.streak += 1
                st.session_state.xp += 10
                st.session_state.coins += 5

                if st.session_state.xp >= st.session_state.level * 50:
                    st.session_state.level += 1
                    st.session_state.xp = 0
                    st.success("⬆ LEVEL UP!")

            else:
                st.error(f"❌ Wrong! {q['ans']}")
                st.session_state.lives -= 1
                st.session_state.streak = 0

    if st.session_state.answered:
        if st.button("➡ Next"):
            st.session_state.q = generate_ai_question(st.session_state.level)
            st.session_state.answered = False
            st.session_state.time = time.time()

# ------------------- GAME OVER -------------------
else:
    st.error("💀 GAME OVER")

    st.markdown(f"<h2 style='color:white;'>Score: {st.session_state.score}</h2>", unsafe_allow_html=True)

    name = st.text_input("Enter your name")

    if st.button("💾 Save Score"):
        save_lb(name, st.session_state.score)
        st.success("Saved!")

    if st.button("🔄 Restart"):
        for k in defaults:
            st.session_state[k] = defaults[k]