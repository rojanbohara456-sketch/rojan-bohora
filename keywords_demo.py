import keyword
print(len(keyword.kwlist))

print(ord('R'))
print(ord('r'))

username="ram"
a=username.maketrans('r','R')
print(a)

age=2+6j
print(age.real)
print(age.imag)


items={*()}
print(type(items))

items1={1,2,3,4}
print(type(items1))
print(id(items1))

items2=[1,2,3]
print(type(items2))

items3={}
print(type(items3))




