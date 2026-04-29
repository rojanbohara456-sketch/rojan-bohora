#TO CHECK IDENTITY
age = 50
print(id(age))
  

#TO CHECK TYPE
print(type(age))


#maths

items = (1,2,3,4,7)
print(len(items))


print(any(items))




a = 2 
b = 3
print({a+b})
print('{} {}'.format(30,40,a=10,b=20))








# #Backslash t (\t)
print('Name\tage\tsalary')
print('Ram\t27\t30000')
print('Shyam\t23\t45000')

# print n
print('&'*10)


#Backslash r (\r)
print("Python\rJava")

#splitiing
employee_records='ram prasad, 13, 29000'
print(employee_records.split(','))

timestamp='2026,12,13'
print(timestamp.split())


#Slicing
stamp = '2026-11-12'
a = stamp.split('-')
print(a)
print(stamp[-7])
print(stamp[8])
print(stamp[0]+stamp[3])

print(stamp[:-3])
print(stamp[3:4])



#only error case
print(stamp[:])



a='Expression'
print(a[11::-6])
print(a[2:-25:-1])
print(a[-15::-2])
print(a[::-1])