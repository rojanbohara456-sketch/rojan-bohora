cart=['apple','orange']
# cart.append('orange')
# cart.extend('orange')
# print(cart)
# cart.insert(0,'chocolate')
# cart.remove(cart[1])
# a=cart.pop(2)
# print(cart)
# print(a)
# cart[0]='coca'
# print(cart)
cart.clear()
print(cart)



numbers={1,2,3,4,5}
numbers.add(4)
numbers.update({9,8})

# numbers.remove(4)

# numbers.discard(8)
# numbers.clear()
print(numbers)
numbers.pop()

print(numbers)
#Empty set 
items={*()}
items=set()
print(type(items))


data1={1,2,3,4,5}
data2={1,2,3,4,5,6,7,8}
data3=data1.difference(data2)
data4=data1.symmetric_difference(data2)
data5=data1.intersection(data2)
data6=data1.union(data2)
data7=data1.isdisjoint(data2)
data8=data1.issubset(data2)
data9=data1.issuperset(data2)
print(data3)
print(data4)
print(data5)
print(data6)
print(data7)
print(data8)
print(data9)



#Dictionary


student_marks= {'ram':99,
                'shyam':88,
                'hari':71}
student_marks['sita']=63
result=student_marks.get('ram')

print(result)
print(student_marks['sita'])

#pop popitem del
student_marks.pop('ram')
print(student_marks)
student_marks.popitem()
print(student_marks)

#keys values items

for i in student_marks:
    print(i)
for i in student_marks.keys():
    print(i)
for i in student_marks.values():
    print(i)
for i in student_marks.items():
    print(i)
for i,j in student_marks.items():
    print(i,'   ',j)

students= {
    'Ram':{'Maths':88, 'Science':99},
    'Shyam':{'Maths':94, 'Science':83},
    'Hari':{'Maths':99, 'Science':80}
}
print(students['Ram']['Maths'])


quiz_data = {
    'qno1':{
        'question':'Which Python library is used fro building desktop GUI ?',
        'options': ['NumPy','Tkinter','Pandas','Flask'],
        'answer':'Tkinter'

    },
    'qno2':{
        'question': 'What is the result of 4==7 in Python ?',
        'options':['True','False','Error','None'],
        'answer':'False'
    },
    'qno3': {
        'question': 'Which set method is used to check if two sets have no common items?',
        'options': ['isalpha',]
    }
}

