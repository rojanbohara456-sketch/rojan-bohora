#Question 1
items = [3,5,7,9,11,13]
remove_items=items.pop(4)
items.insert(2,remove_items)
items.append(remove_items)
print(items)


#Question 2
first_set= {23,42,65,57,78,83,29}
second_set={57,83,29,67,73,43,48}

common_elements=first_set.intersection(second_set)
print(common_elements)
if common_elements:
    print(f'common elements: {common_elements}')
    unique_elements=first_set.symmetric_difference(second_set)
    print(unique_elements)

else:
    print('No common elements')



#Question 3
set1={27,43,34}
set2={34,93,22,27,43,53,48}

subset=set1.issubset(set2)
print(subset)
if subset:
    set3=set2-set1
    print(set3)
else:
    print('It is not subset')
superset=set1.issuperset(set2)
print(superset)



#Question 4
month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53,
         'july': 54, 'Aug': 44, 'Sept': 54}

values = []
for key in month:
    if month[key] not in values:
        values.append(month[key])

print(values)


#Question 5
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique = []
for i in sample_list:
    if i not in unique:
        unique.append(i)


unique_tuple = tuple(unique)


minimum = unique[0]
maximum = unique[0]
for num in unique_tuple:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Tuple:", unique_tuple)
print("Minimum:", minimum)
print("Maximum:", maximum)




#question 6

club_A = ["ram", "hari", "shyam"]
club_B = ["ram", "gita", "hari"]

common = []
for member in club_A:
    if member in club_B:
        common.append(member)

if len(common) > 0:
    print("the following members exist in both groups:", common)
else:
    print("no overlapping members found between groups")


#Question 7


required_tasks  = ["Email", "Report", "Meeting"]
completed_tasks = ["Email", "Report"]

all_done = True
for task in required_tasks:
    if task not in completed_tasks:
        all_done = False
        break

if all_done:
    print("all tasks done")
else:
    print("some tasks pending")




