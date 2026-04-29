#method 1
username='Laxman devKota'
as_v=username.maketrans('L K','l_k')
print(username.translate(as_v))
#method 2
username='Laxman devKota'
print(username.replace('L','l').replace(' ','_').replace('K','k'))
#method 3
username='Laxman devKota'
print(username.lower().replace(' ','_'))

first_name='ram'
middle_name='bahadur'
last_name='kc'
#ram_bahadur_kc
#method 1
print(f'{first_name}_{middle_name}_{last_name}')

#method 2
print('_'.join([first_name,middle_name,last_name]))

#method 3
print(first_name + '_' + middle_name + '_' + last_name)

full_name = 'ram bahadur kc'
print(full_name.title())

