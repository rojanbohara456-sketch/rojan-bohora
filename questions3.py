'''
age=eval(input('enter your age: '))
print(type(age))
'''
'''
year=2026
month=12
days=31
print(year,month,days,sep='/')
print(f'{year}/{month}/{days}')
print('/'.join([str(year), str(month), str(days)]))
print('{2}/{1}/{0}'.format(year,month,days))

'''
items=['apple','banana','orange']
for i in items:
    print(i)