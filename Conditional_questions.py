#1. Write a program to check whether the given number is in between 1 and 100 or not.
number = int(input("Enter a number: "))
if 1 < number < 100:
    print(f"{number} is between 1 and 100.")
else:
    print(f"{number} is not between 1 and 100.")

#2. Check whether the given number is even or odd and display it to the user.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

#3 Write a program that asks the user for a number in the range of 1 to 12. the program should display the corresponding month, where 1 is January, 2 is February, and so on. If the user enters a number outside the range, the program should display an error message.
 
month_number = int(input("Enter a number between 1 and 12: "))
#Method 1
if month_number == 1:
    print("January")
elif month_number == 2:
    print("February")
elif month_number == 3:
    print("March")
elif month_number == 4:
    print("April")
elif month_number == 5:
    print("May")
elif month_number == 6:
    print("June")
elif month_number == 7:
    print("July")
elif month_number == 8:
    print("August")
elif month_number == 9:
    print("September")
elif month_number == 10:
    print("October")
elif month_number == 11:
    print("November")
elif month_number == 12:
    print("December")
else:
    print("Error: Please enter a number between 1 and 12.")

#Method 2
months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}
month_number = int(input("Enter a number between 1 and 12: "))
if month_number in months:
    print(months[month_number])
else:    print("Error: Please enter a number between 1 and 12.")

#Method 3
month_number = int(input("Enter a number between 1 and 12: "))
if 1 <= month_number <= 12:
    month_name = ["January", "February", "March", "April", "May", "June", 
                  "July", "August", "September", "October", "November", "December"]
    print(month_name[month_number - 1])
else:
    print("Error: Please enter a number between 1 and 12.")







#4. A school has the following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
#Ask user to enter marks and print the corresponding grade based on the above rules.
marks = int(input("Enter your marks: "))
if marks < 25:
    print("Grade: F")
elif 25 <= marks < 45:
    print("Grade: E")
elif 45 <= marks < 50:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: C")
elif 60 <= marks < 80:
    print("Grade: B")
elif marks >= 80:
    print("Grade: A")
else:
    print("Invalid marks entered.")




#5. Write a program to check whether a number is divisible by 7 or not.
number = int(input("Enter a number: "))
if number % 7 == 0:
    print(f"{number} is divisible by 7.")
else:
    print(f"{number} is not divisible by 7.")


#6. Write a program to accept 2 numbers and mathematical operators and perform the operation accordingly.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
if operator == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator entered.")

#7. Write a Python program to check car loan eligibility: Salary>= 50000 and Credit score >= 700:
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
if salary >= 50000 and credit_score >= 700:
    print("eligible for a car loan.")
else:
    print("not eligible for a car loan.")


#8. Write a Python program that takes an integer input n n. From given number, check if it is divisible by both 3 and 5, and print "FizzBuzz" if true. If the number is divisible only by 5, print "Buzz." If it is divisible only by 3, print "Fizz." Finally, if the number is not divisible by either 3 or 5, print the number itself.
n = int(input("Enter an integer: "))
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)

#9. Write a Python program that takes a character input and checks whether it is a vowel or consonant.
character = input("Enter a character: ").lower()
if character in 'aeiou':
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

#10. Write a Python program to input marks and determine the grade based on the following conditions:
# 90-100: A
# 80-89: B
# 70-79: C
# Below 70: Fail

marks = int(input("Enter your marks: "))
if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks < 90:
    print("Grade: B")
elif 70 <= marks < 80:
    print("Grade: C")
else:
    print("Grade: Fail")

#11. Write a Python program to categorize a person’s age:

#Age < 13: Child

#13 <= Age <= 19: Teenager

#Age > 19: Adult
age = int(input("Enter your age: "))
if age < 13:    
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")


#12.Write a Python program to check if a given character is uppercase, lowercase, or a digit.
character = input("Enter a character: ")
if character.isupper():
    print("The character is uppercase.")
elif character.islower():
    print("The character is lowercase.")
elif character.isdigit():
    print("The character is a digit.")
else:
    print("The character is not an uppercase letter, lowercase letter, or digit.")


#13. Write a Python program that takes a color as input ("Red", "Yellow", "Green") and outputs the corresponding action ("Stop", "Get Ready", "Go").

color = input("Enter a traffic light color (Red, Yellow, Green): ").lower()
if color == "red":  
    print("Stop")
elif color == "yellow":
    print("Get Ready") 
elif color == "green":
    print("Go")
else:
    print("Invalid color entered. Please enter Red, Yellow, or Green.")


#14. 14. Write a Python program to check eligibility for a job based on age and experience:

#Age > 18 and Experience >= 2 years: Eligible

#therwise: Not Eligible
age = int(input("Enter your age: "))
experience = int(input("Enter your years of experience: ")) 
if age > 18 and experience >= 2:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")


#15. Write a Python program to give advice based on the temperature:

#Temperature > 30°C: "It's hot, stay hydrated!"

#Temperature between 15-30°C: "Enjoy the weather!"

#Temperature < 15°C: "It's cold, wear warm clothes!"

temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's hot, stay hydrated!")
elif 15 <= temperature <= 30:
    print("Enjoy the weather!")
else:
    print("It's cold, wear warm clothes!")


#16. Write a Python program that takes a menu option ("Pizza", "Burger", "Pasta") and prints its price:

#Pizza: $10

#Burger: $7

#Pasta: $8

menu_option = input("Enter a menu option (Pizza, Burger, Pasta): ").lower()
if menu_option == "pizza":
    print("Price: $10")
elif menu_option == "burger":
    print("Price: $7")
elif menu_option == "pasta":
    print("Price: $8")
else:
    print("Invalid menu option entered. Please enter Pizza, Burger, or Pasta.")



#17. Write a Python program to select players based on height:

#Height >= 6 feet: Selected

#Height < 6 feet: Not Selected

height = float(input("Enter your height in feet: "))
if height >= 6:
    print("You are selected.")
else:
    print("You are not selected.")





#18. Write a Python program to check if a person is eligible to watch a movie based on their age:

#Age >= 18: Allowed

#Age < 18: Not Allowed

age = int(input("Enter your age: "))
if age >= 18:
    print("You are allowed to watch the movie.")
else:
    print("You are not allowed to watch the movie.")




#19. Write a Python program to check login credentials:

#Username: "admin", Password: "password123"

#If correct, print "Access Granted"; otherwise, print "Access Denied."

username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Access Granted")
else:
    print("Access Denied")



#20. Write a Python program that takes a month number (1–12) and outputs the corresponding season:

#12, 1, 2: "Winter"

#3, 4, 5: "Spring"

#6, 7, 8: "Summer"

#9, 10, 11: "Autumn"

month_number = int(input("Enter a month number (1-12): "))
if month_number in [12, 1, 2]:
    print("Season: Winter")
elif month_number in [3, 4, 5]:
    print("Season: Spring")
elif month_number in [6, 7, 8]:
    print("Season: Summer")
elif month_number in [9, 10, 11]:
    print("Season: Autumn")
else:
    print("Invalid month number entered. Please enter a number between 1 and 12.")
