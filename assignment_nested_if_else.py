#1. A theme park has these rules: You can ride the roller coaster if you are at least 12 years old and at least 140 cm tall.
age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))
if age >= 12 and height >= 140:
    print("You can ride the roller coaster!")
else:
    print("You do not meet the requirements to ride the roller coaster.")

#2. Desgin a Traffic light System. Given a variable light that can be "red", "yellow", or "green", print the correct instruction. also handle invalid color with an error message.

light = input("Enter the traffic light color (red, yellow, green): ")
match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color entered. Please enter red, yellow, or green.")
        
        
#3. Write a match statement that takes a number 1-4 and prints the corresponding season (1: Spring, 2: Summer, 3: Fall, 4: Winter). Default: 'unknown'.
number = int(input("Enter a number (1-4): "))
match number:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Fall")
    case 4:
        print("Winter")
    case _:
        print("Unknown")
    

#4. Write a login system using nested if. Check -if the username equals "admin", inside that, if the password equals "pass123" print appropriate messages for: valid login, wrong password, and wrong username.
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin":
    if password == "pass123":
        print("Valid login")
    else:
        print("Wrong password")
else:
        print("Wrong username")

#5. Design a bank loan approval system. approve a loan only if all three conditions are met: age is between 21 and 60 (inclusive), monthly income is at least 30000, credit score is at least 700. If not approved, print which condition failed. If multiple fail, pick the most improtant one to report.

age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
credit_score = int(input("Enter your credit score: "))
if age < 21:
    print("Loan not approved: Age must be at least 21.")
elif age > 60:
    print("Loan not approved: Age must be 60 or younger.")
elif income < 30000:
    print("Loan not approved: Monthly income must be at least 30000.")
elif credit_score < 700:
    print("Loan not approved: Credit score must be at least 700.")
else:
    print("Loan approved!")

#6. You are developing a simple ticket booking depends on the age of the person and whether they have a membership card. If the person is under 12, the ticket is free. If the person is between 12 and 60: If they have a membership card, the ticket costs Rs. 150. If not, the ticket costs Rs. 200. If the person is above 60, they get a senior citizen discount, and the ticket costs Rs. 100. Write a Python program using nested if-else to calculate and print the ticket price based on the user's age and membershipstatus.
age = int(input("Enter your age: "))
membership_card = input("Do you have a membership card? (yes/no): ").lower()
if age < 12:
    print("Ticket price: Free")
elif 12 <= age <= 60:
    if membership_card == "yes":
        print("Ticket price: Rs. 150")
    else:
        print("Ticket price: Rs. 200")
else:
    print("Ticket price: Rs. 100 (Senior citizen discount)")

#7. A company decided to give a bonus of 5% to employee if his/her years of service is more than 5 years ask user for their salary and year of service and print the the net bonus amount.
salary = float(input("Enter your salary: "))
years_of_service = int(input("Enter your years of service: "))
if years_of_service > 5:
    bonus = salary * 0.05
    print(f"Congratulations! You are eligible for a bonus of Rs. {bonus:.2f}")
else:
    print("Sorry, you are not eligible for a bonus.")

#8. Write a python program which accepts the radius of circle from user and compute the area.
radius = float(input("Enter the radius of the circle: "))
area = 3.14 * radius ** 2
print(f"The area of the circle with radius {radius} is: {area:.2f}")

#9. | Age           | Gender | Wage/day |
#| ------------- | ------ | -------- |
#| >=18 and <30  | M      | 700      |
#|               | F      | 750      |
#| >=30 and <=40 | M      | 800      |
#|               | F      | 850      |
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ").upper()
if age >= 18 and age < 30:
    if gender == "M":
        print("Your wage per day is Rs. 700")
    elif gender == "F":
        print("Your wage per day is Rs. 750")
elif age >= 30 and age <= 40:
    if gender == "M":
        print("Your wage per day is Rs. 800")
    elif gender == "F":
        print("Your wage per day is Rs. 850")
else:
    print("You are not eligible for this wage scale.")

#10. Accept input from user
# If given number is a multiple of both 3 and 5 prints "Fizz Buzz" instead of number
# If given number is a multiple of 3 but not 5 prints "Fizz" instead of number
# If given number is a multiple of 5 but not 3 prints "Buzz" instead of number
# If given number is not multiple of 3 or 5 prints value as usual.

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
    
