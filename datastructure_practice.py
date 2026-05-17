# #Question 1

# students_data = {
#     'id_no_1': {'name': 'Rahul', 'email': 'rahul@gmail.com'},
#     'id_no_2': {'name': 'Max', 'email': 'max@gmail.com'},
#     'id_no_3': {'name': 'Cris', 'email': 'cris@gmail.com'}
# }

# name = input('Enter your name: ')
# found = False
# for student in students_data.values():
#     if student['name'].lower() == name.strip().lower():
#         print(f"Email: {student['email']}")
#         found = True
        

# if not found:
#     print("Contact not found")



# #Question 2
# shopping_list={'Milk','Bread','Eggs'}
# bought={'Bread','Eggs'}

# unbought_items=shopping_list.difference(bought)

# if unbought_items==set():
#     print("Shopping Completed!")
# else:
#     print(f'items remaining:{unbought_items} ')


# #Question 3
# class_list=['ram','sita','laxman']
# new_student=input('enter the name of student to be added:')
# if new_student in class_list:
#     print("Student already in the lsit")
# else:
#     class_list=class_list.append(new_student)
#     print(f'{new_student} was added in the class list')

# #Questionn 4
# votes=['Blue','Red','Blue','Green','Blue']
# occurence=votes.count('Blue')
# if occurence>=3:
#     print('Blue won')
# else:
#     print('Blue did not win')


# #question 5
# grades={'Ram':92,'Sita':88}
# student_name=input("Enter Student's Name:")
# if student_name in grades:
#     print(f"Grade for {student_name}: {grades[student_name]}")
# else:
#     print(f"Grade not available for '{student_name}'.")


# # Question 6
# applicant={'name':'Priya', 'skills':['Java','SQL'], 'experience_year':1}
# required_skills={'Python','Java'}
# common_skills=required_skills.intersection(set(applicant['skills']))
# if common_skills in required_skills:
#     print("the applicant: Priya is qualified")
# else:
#     print('Priya is not qualified')

#Question 7
banned_items={'scissors','knife','lighter'}
baggage_weight=int(input("Enter the weight of the Baggage: "))
items_in_baggage=input("Enter the items in baggage: ").lower()

if baggage_weight<=7 and items_in_baggage not in banned_items :
    print("The bag is allowed")
else:
    print("The bag is not allowed")



#Question 8
sample_dict = { 
    'emp1': {'name':'Jhon', 'salary':7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Shyam', 'salary': 500}
}
for emp in sample_dict.values():
    if emp['name'] == 'Shyam':
        emp['salary'] = 8500

print(sample_dict)

#Question 9
ram_items = {"apple", "banana", "mango", "grape"}
hair_items = {"orange", "pineapple", "watermelon", "papaya"}
if ram_items.isdisjoint(hair_items):
    print("They picked completely different items")
else:
    print("They have some common items")

#Question 10

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 15, 20}
my_dict = {'a': 10, 'b': 20}
val = 20

if val in my_list and val in my_tuple:
    if 'b' in my_dict and val not in my_set:
        print("Verified Token Routed")
        print("Path A")
    else:
        print("Access Denied / Route Diverted")
        print("Path B")

else:
    print("System Rejects Token")
    print("Path C")



#Question  16
menu = {
    'Pizza': 450,
    'Burger': 300,
    'Salad': 200
}
order = 'Pizza'

if order in menu:
    print(f"The price of {order} is Rs{menu[order]}")
else:
    print("Item not found")

# Question 17
student_data = {"name": "Sam", "score": 85}
if student_data["score"] >= 80:
    student_data["status"] = "Pass"
else:
    student_data["status"] = "Review"

print(student_data)

#Question 18
database = {"admin": "1234", "user": "abcd"}
user_input = 'admin'
user_pass = '1234'

if user_input in database and database[user_input] == user_pass:
    print("Login Successful")
else:
    print("Login Failed")

#Question 19
emails = ['ram123@gmail.com', 'hari77@gmail.com']
blacklisted_emails = {'hari77@gmail.com'}
current_email = 'hari77@test.com'

if current_email in emails and current_email not in blacklisted_emails:
    print("Email Sent")
else:
    print("Blocked")


#Question 20
inventory        = {'A1': 50, 'B2': 0, 'C3': 10}
restricted_zones = {'B2', 'Z9'}
target           = 'B2'


if target in inventory:
    if target not in restricted_zones and inventory[target] > 0:
        print("dispatch item")
    else:
        print("stock error")

else:
    print("invalid zone")
    




# Question 21
valid_courses= {'python', 'robotics', 'java'}
hs_grades = [9, 10, 11, 12]

name   = input("Enter student name: ")
course = input("Enter course (python/robotics/java): ").lower()
grade  = int(input("Enter grade (9-12): "))

student_record = {
    "name"  : name,
    "course": course,
    "grade" : grade
}
if course not in valid_courses:
    print(f"{name} selected an invalid course.")

elif grade < 9:
    print(f"Grade too low.")

elif grade > 12:
    print(f"Grade too high.")

else:
    if course == 'robotics' and grade == 9:
        print(f"{name} is not eligible for {course}, grade too low.")
    else:
        print(f"{name} is approved for {course}.")
