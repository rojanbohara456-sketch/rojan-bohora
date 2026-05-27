
#Question 1

for number in range(1, 6):
    if number % 2 == 0:
        print(f"Number {number} is even.")
    else:
        print(f"Number {number} is odd.")

#Question 2

numbers = [10, 20, 30, 40]
total = 0

for value in numbers:
    total += value
    print(f"Added {value}. Running total is {total}.")

print(f"Total Sum: {total}")

#Question 3
student_names = ["Ram", "Hari", "Sita"]

print("--- Email Greetings Generated ---")
for name in student_names:
    print(f"Hi {name}, your course approval is ready!")

#Question 4
pages = [45, 30, 50, 40]

print("--- Book Chapter Summary ---")
for i, page in enumerate(pages, start=1):
    print(f"Chapter {i} has {page} pages.")

#Question 5
lst = [4, 5, 3, 2]

product = 1
for num in lst:
    product *= num

print("Product of all elements:", product)

#Question 6
number = 11

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

#Question 7
lst = [3, 2, 1, 4, 5]

reversed_lst = lst[::-1]
print("Reversed list:", reversed_lst)

#Question 8
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []
for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)


#Question 9
lst = [1, 2, 3, 4]

print(lst[0])
print(lst[-1])

#Question 10
string = "Hello World"
vowels = "aeiou"

result = ""
for char in string:
    if char not in vowels:
        result += char

print("String without vowels:", result)

#Question 11
sentence = "Loops are Fun"

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("vowels:", vowel_count)
print("consonants:", consonant_count)


#Question 12
lst = [1, 2, 3, 4, 5]

odd = []
even = []

for num in lst:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Odd:", odd)
print("Even:", even)

#Question 13 
number = 29

is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

#Question 14
number = 29

is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")


#Question 15

s = "Hello123"  
 
digits = 0
letters = 0
 
for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
 
print(f"String: '{s}'")
print(f"Digits: {digits}")
print(f"Letters: {letters}")


#Question 16
 
valid_username = "admin"
valid_password = "1234"
username = "admin"
password = "1234"
 
print("Username:", username)
print("Password:", password)
 
if username == valid_username and password == valid_password:
    print("Login successful!")
else:
    print("Invalid username or password.")
 
 
 
#Question 17
 
number = 7  
 
print(f"{number} is", "Even." if number % 2 == 0 else "Odd.")
 
 
#Question 18

number = 5  
 
factorial = 1
for i in range(1, number + 1):
    factorial *= i
 
print(f"Factorial of {number} is {factorial}")
 
 
#Question 19
 
print("Multiplication Tables (1 to 8):")
for num in range(1, 9):
    print(f"--- Table of {num} ---")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
 
 
#Question 20
lst = [1, 2, 3, 4]
 
print("First element:", lst[0])
print("Second element:", lst[1])
 
 
#Question 21
 
start = 1
end = 10
 
total = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        total += num
 
print(f"Sum of odd numbers from {start} to {end}: {total}")
 
 
#Question 22
 
start = 1
end = 10
 
total = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        total += num
 
print(f"Sum of even numbers from {start} to {end}: {total}")
 
 
#Question 23
 
s = "Hello World Python"
 
count = 0
for char in s:
    if char == " ":
        count += 1
 
print(f"String: '{s}'")
print(f"Number of spaces: {count}")
 
 
#Question 24
 
lst = [1, 2, 3, 4]
 
result = []
for num in lst:
    result.append(num ** 3)
 
print("Original list:", lst)
print("Cubed list:", result)
 
 
#Question 25
 
a = "programming"
 
reversed_str = a[::-1]
print(f"Original string: {a}")
print(f"Reversed string: {reversed_str}")
 
 
#Question 26
 
print("Numbers from 0 to 7:")
for i in range(50):
    print(i)
    if i == 7:
        break
 
 
#Question 27
word = "Python"
 
print("Letters in the string:")
for letter in word:
    print(letter)
 
 
#Question 28
 
a = ["ram", "shyam", 1, 2]
 
print("Greetings:")
for item in a:
    if type(item) == str:
        print(f"Hello!{item}")
 
 
#Question 29
 
a = ["ram", "shyam"]
lst = []
 
for item in a:
    lst.append(f"Dr.{item}")
 
print("List with Dr. prefix:", lst)
 
 
#Question 30
 
numbers = [1, 2, 3, 4, 5]
squares = []
 
for num in numbers:
    squares.append(num ** 2)
 
print("Original:", numbers)
print("Squares:", squares)
 
 
#Question 31
 
lst1 = [111, 32, -9, -45, -17, 9, 85, -10]
lst2 = []
 
for num in lst1:
    if num > 0:
        lst2.append(num)
 
print("Original:", lst1)
print("Positive numbers:", lst2)
 
 
#Question 32
 
lst = [0, 1, 2, 3, 4, 5, 6]
 
print("Numbers (excluding 3 and 6):")
for num in lst:
    if num == 3 or num == 6:
        continue
    print(num)
 
 
#Question 33
 
list1 = [1, "hello", 3.14, True]
list2 = []
 
for item in list1:
    list2.append(type(item))
 
print("Original list:", list1)
print("Types list:", list2)
 
 
#Question 34
 
fruits = ["apple", "banana", "cherry"]
 
print("Fruits:")
for fruit in fruits:
    print(fruit)
else:
    print("Done")
 
 
#Question 35
 
print("Series (105 to 7, step -7):")
for num in range(105, 0, -7):
    print(num, end=" ")
print()
 
 
#Question 36
 
bad_chars = [';', ':', '!', '*', ' ']
string = "py;th* o:n ! ;py * t*h:o !n"
 
result = ""
for char in string:
    if char not in bad_chars:
        result += char
 
print("Original string:", string)
print("Cleaned string:", result)
 
 
#Question 37
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
even_count = 0
odd_count = 0
 
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
 
print("Numbers:", numbers)
print(f"Even count: {even_count}")
print(f"Odd count: {odd_count}")
 
 
#Question 38
 
total = 0
 
for num in range(3, 100):
    if num % 3 == 0 or num % 5 == 0:
        total += num
 
print("Sum of multiples of 3 or 5 (3 to 99):", total)
 
 
#Question 39
 
even_sum = 0
odd_sum = 0
 
for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num
 
print("Sum of even numbers (1-100):", even_sum)
print("Sum of odd numbers (1-100):", odd_sum)


#Question 40
list1 = [10, 20, 10, 30, 10, 40, 50]
target = 10

count = 0
for num in list1:
    if num == target:
        count += 1

print(f"{target} appears {count} time(s)")
