
#Method 1
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = input("Enter your email: ")
# re_email = input("Re-enter your email: ")
# password = input("Enter your password: ")
# if not (first_name and last_name and email and re_email and password):
#     print("All fields are required")
# elif not (first_name.isalpha() and last_name.isalpha() and "@" in email and "." in email and email == re_email and len(password) >= 6):
#     print("Invalid input")

# else:    
#     print("Valid input")

#Method 2
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = input("Enter your email: ")
# re_email = input("Re-enter your email: ")
# password = input("Enter your password: ")





# if last_name=="":
#     print("last name cannot be empty")  
# elif not last_name.isalpha():
#     print("must enter letters only")
# else:
#     print("valid")

# email = input("Enter your email: ")
# if email=="":
#     print("email cannot be empty")
# elif "@" not in email or "." not in email:
#     print("invalid email format")
# else:
#     print("valid")

# re_email = input("Re-enter your email: ")
# if re_email=="":
#     print("email cannot be empty")

# elif re_email != email:
#     print("emails do not match")
# else:
#     print("valid")

# password = input("Enter your password: ")
# if password=="":
#     print("password cannot be empty")
# elif len(password) < 6:
#     print("password must be at least 6 characters long")
# else:
#     print("valid")

#Method 3
# first_name1 = input("Enter your first name: ")
# last_name1 = input("Enter your last name: ")
# email1 = input("Enter your email: ")
# re_email1 = input("Re-enter your email: ")
# password1 = input("Enter your password: ")

# if not (first_name1 and last_name1 and email1 and re_email1 and password1):
#     print("All fields are required")
# elif not (first_name1.isalpha() and last_name1.isalpha()):
#     print("First name and last name must contain only letters")
#     is_valid = False
# elif "@" not in email1 or "." not in email1:
#     print("Invalid email format")
#     is_valid = False
# elif email1 != re_email1:
#     print("Emails do not match")
#     is_valid = False
# elif len(password1) < 6:
#     print("Password must be at least 6 characters long")
#     is_valid = False
# else:
#     print("Valid input")
#     is_valid = True


# number = int(input("Enter a number: "))
# if number ==1:
#     print("Spring")
# elif number ==2:
#     print("Summer")
# else:
#     print("Invalid number")

# #or

# match number:
#     case 1:
#         print("Spring")
#     case 2:
#         print("Summer")
#     case _:
#         print("Invalid number")

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = input("Enter your email: ")
# re_email = input("Re-enter your email: ")
# password = input("Enter your password: ")

# if first_name == "":
#     print("First name cannot be empty")
# elif not first_name.isalpha():
#     print("First name must contain only letters")
# else:
#     print("Valid first name")

# if last_name == "":
#     print("Last name cannot be empty")
# elif not last_name.isalpha():
#     print("Last name must contain only letters")
# else:
#     print("Valid last name")

# if email == "":
#     print("Email cannot be empty")
# elif "@" in email and "." in email:
#     print("Invalid email")
# else:
#     print("Valid email")

# if re_email == "":
#     print("Re-entered email cannot be empty")
# elif re_email != email:
#     print("Emails do not match")
# else:
#     print("Emails match")

# if password == "":
#     print("Password cannot be empty")
# elif len(password) < 6:
#     print("Password must be at least 6 characters long")
# else:
#     print("Valid password")

# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# email = input("Enter your email: ")
# re_email = input("Re-enter your email: ")
# password = input("Enter your password: ")

# if not (first_name and last_name and email and re_email and password):
#     print("All fields are required")
# elif not (first_name.isalpha() and last_name.isalpha()):
#     print("First name and last name must contain only letters")
# elif not (("@" in email and "." in email) and ("@" in re_email and "." in re_email)):
#     print("Invalid email format")
# elif email != re_email:
#     print("Emails do not match")
# elif len(password) < 6:
#     print("Password must be at least 6 characters long")
# else:
#     print("Registration successful!")



#Hand sign game
# hand_sign_P1 = input("Player 1, enter your hand sign (rock, paper, scissors): ")
# hand_sign_P2 = input("Player 2, enter your hand sign (rock, paper, scissors): ")
# if hand_sign_P1 == hand_sign_P2:
#     print("It's a tie!")
# elif (hand_sign_P1 == "rock" and hand_sign_P2 == "scissors") or (hand_sign_P1 == "paper" and hand_sign_P2 == "rock") or (hand_sign_P1 == "scissors" and hand_sign_P2 == "paper"):
#     print("Player 1 wins!")
# elif (hand_sign_P2 == "rock" and hand_sign_P1 == "scissors") or (hand_sign_P2 == "paper" and hand_sign_P1 == "rock") or (hand_sign_P2 == "scissors" and hand_sign_P1 == "paper"):
#     print("Player 2 wins!")


#ATM money withdrawal
# balance = 20000
# correct_pin = 3796

# print("Welcome to the Global Bank ATM!")
# user_pin = int(input("Please enter your 4-Digit PIN: "))
# if user_pin == correct_pin:
#     print("1. Check Balance")
#     print("2. Withdraw Money")
#     print("3. Exit")

#     choice = int(input("Please select an option(1-3): "))

#     if choice == 1:
#         print(f"Your balance is: Rs.{balance}")
#     elif choice == 2:
#         amount = int(input("Enter the amount you want to withdraw: "))
#         if amount <= balance:
#             balance -= amount
#             if amount <= 0:
#                 print("Invalid amount")

#             print(f"Please take your cash: Rs.{amount}")
#             print(f"Your new balance is: Rs.{balance}")

#         else:
#             print("Insufficient funds")
#     elif choice == 3:
#         print("Thank you for using the Global Bank ATM!")
#     else:
#         print("Invalid option")
# else:
#     print("Incorrect PIN. Please try again.")

#Game: Bingo
number = int(input("Enter a number between 1 and 100: "))
if number < 1 or number > 100:
    print("Invalid number. Please enter a number between 1 and 100.")
elif number % 3 == 0 and number % 5 == 0:
    print("Bingo")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Try again")


#Method 1


#Method 2
# import random
# hand_signs = ["rock", "paper", "scissors"]
# hand_sign_P1 = input("Player 1, enter your hand sign (rock, paper, scissors): ")
# hand_sign_P2 = random.choice(hand_signs)
# print(f"Player 2 chose: {hand_sign_P2}")
# if hand_sign_P1 == hand_sign_P2:
#     print("It's a tie!")
# elif (hand_sign_P1 == "rock" and hand_sign_P2 == "scissors") or (hand_sign_P1 == "paper" and hand_sign_P2 == "rock") or (hand_sign_P1 == "scissors" and hand_sign_P2 == "paper"):
#     print("Player 1 wins!")
# elif (hand_sign_P2 == "rock" and hand_sign_P1 == "scissors") or (hand_sign_P2 == "paper" and hand_sign_P1 == "rock") or (hand_sign_P2 == "scissors" and hand_sign_P1 == "paper"):
#     print("Player 2 wins!")
# else:
#     print("Invalid input. Please enter rock, paper, or scissors.")

#Elevator program
floor = int(input("Enter the floor number (1-10): "))
if floor < 1 or floor > 10:
    print("Invalid floor number. Please enter a number between 1 and 10.")
elif:
    print(f"Elevator is going to floor {floor}. Please wait...")


    weight = int(input("Enter the weight of the passengers in kg: "))
    if weight > 500:
     if weight <= 0:
      print("Invalid weight. Please enter a valid weight.")
     print("Weight limit exceeded. Lift cannot operate.")
    elif:
    print("Lift is operating. Please wait...")

    elif:
    door_status = input("Is the elevator door open or closed? (open/closed): ")
    if door_status == "open":
      print("Please close the door before operating the elevator.")
    elif door_status == "closed":
      print("Door is closed. Elevator is operating. Please wait...")











