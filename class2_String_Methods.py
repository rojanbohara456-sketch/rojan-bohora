#formating method [format() Method]

name ='ram'
age = 29
print('{} {}'.format(name,age))

n1 = 12
n2 = 21
#print('{n1+n2}'.format(n1,n2)) [Not possible]


#f-string method

print(f'{name}{age}')


name1 = 'Shyam'
print(name1.replace('S','s'))
p_n = '+977+11'
print(p_n[0:4]+ p_n[5:])

count = 0
p_n = '+977+11'
f_r = '+977+11'

for i in range(len(p_n)):
    if p_n[i]=='+':
        count = count+1
        if count==2:
            continue

f_r = f_r + p_n[i]



price='$12.77'
print(price.replace('$',''))
           
p_l='python'
#print(p_l.replace('p','P').replace('n','N'))

as_v = p_l.maketrans('pn','PN')
print(p_l.translate(as_v))


#skey value lower case a-z = 97-
 #upper case A-Z = 65-
 #0-9 = 48-57


key='print'
print(key.center(13,'*'))

key1='printed'
print(key1.ljust)

#starts with
url='https:web.gmail.com'
print(url.startswith('.xxlx'))
if url.startswith('.xllx'):
    print('valid url')
else:    print('invalid url')



#find rfind index rindex 

dataset='python is a programming language'
print(dataset.find('a'))
print(dataset.rfind('a'))
print(dataset.index('a'))
print(dataset.rindex('a'))

dataset2='ram is a boy'
print(dataset2.find('r'))

index_number = dataset2.rfind('r')
print(index_number-len('dataset2'))
print(dataset2.rfind('r'))
print(dataset2.index('r'))
print(dataset2.rindex('r'))
















