
'''
Control flow 
1.	Conditional statement [if/ eilf/ else]
2.	Iterative statements [for loop/ while loop]
3.	Transfer statements 


Conditional statements
-Acts as a decision maker.
Basic structures:
if condition:
    runs if condition is true
elif condition:
    runs if condition is true
else:
    runs if condition is false

'''
age = 18
if age >= 18:
    print("You are an adult.")

temperature = 35
if temperature > 30:
    print("It's a hot day.")
    print("Drink plenty of water.")
else:
    print("It's a pleasant day.")
    print("Enjoy your day!")

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else score < 60:
    print("Grade: F")
    print("Keep trying!")

# without if else
balance = 10000
amount = int(input("Enter withdrawal amount: "))

balance = balance - amount
print(f"Your new balance is: {balance}")

#without if else, the code will always subtract the amount from the balance, even if the amount is greater than the balance or if the amount is negative. This can lead to incorrect results and potential issues with the account balance.



# with if else
balance1 = 10001

amount1 = int(input("Enter withdrawal amount: "))

if amount1 > balance1:
    print("Insufficient funds.")
elif amount1 <= 0:
    print("Invalid amount.")
else:
    balance1 = balance1 - amount1
    print(f"Your new balance is: {balance1}")

#with if else, the code checks if the withdrawal amount is greater than the balance or if it is negative before performing the subtraction. This ensures that the account balance is only updated when the withdrawal amount is valid and there are sufficient funds available.


#with if else
correct_password = "secret123"
user_input = input("Enter the password: ")
if user_input == correct_password:
    print("Access granted.")
elif user_input != correct_password:
    print('user_input is not correct')
else:
    print("Access denied. Incorrect password.")

#without if else
correct_password1 = "secret123"
user_input1 = input("Enter the password: ")

entered_password = user_input1 == correct_password1
print("Access granted.")

#without if else
Name= "Ram"
age = 13

print(f"{Name} registered to vote.") 
print('Voter id issued')

#with if else
Name1= "Shyam"
age1 = 17
if age1 >= 18:
    print(f"{Name1} registered to vote.") 
    print('Voter id issued')   
else:
    print(f"Must be at least 18 to register to vote.")
    print(f"{Name1} is not eligible to vote.")














