#1. Write a program that prompts the user to input a series of numbers until they input a duplicate number. Use a while loop to check for duplicates.
input_number = []

while True:
    num = int(input("Enter a number: "))
    if num in input_number:
        print(f"Duplicate found: {num}. Stopping.")
        break
    input_number.append(num)


#2. Write a program that prompts the user to enter a positive integer. It then calculates and prints the factorial of that number using a while loop.
n = int(input("Enter a positive integer: "))

factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")

#3. Write a program that accepts a number from the user and calculates the sum of all numbers from 1 up to that number.
n = int(input("Enter a number: "))

total = 0
i = 1

while i <= n:
    total += i
    i += 1

print(f"Sum from 1 to {n} = {total}")

#4. Given a list of numbers, use a loop to count how many times a specific number for example 10 appears.
numbers = [10, 4, 3, 8, 10, 7, 10, 5, 2, 10]
target = 10
count = 0

for num in numbers:
    if num == target:
        count += 1

print(f"{target} appears {count} times")

#5. Write a program that counts the total number of vowels and consonants in a given sentence, ignoring spaces and special characters.
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

#6. Write a program to count the total number of digits in a given integer
n = int(input("Enter an integer: "))
count = 0

while n > 0:
    n //= 10
    count += 1

print(f"Total digits: {count}")

#77. Generate a sequence until it reaches 1. If you start with any positive integer n, and
    #if n is even, divide it by 2; if n is odd, multiply it by 3 and add 1. Repeat the process.
    #The sequence will always eventually reach 1. Write a program to print this
    #sequence for a given number.
    #given input: n = 6
    #expected output: 6, 3, 10, 5, 16, 8, 4, 2, 1

n = int(input("Enter a positive integer: "))

while n != 1:
    print(n, end=", ")
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1

print(n)

#8. Print alphabet Series from A–Z
i = 65

while i <= 90:
    print(chr(i), end=" ")
    i += 1


#9. Write a program that prompts the user for a starting integer and an ending integer. 
# Use a while loop to print all numbers between them, inclusive.

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

i = start

while i <= end:
    print(i, end=" ")
    i += 1

#10. Write a program that prints all odd numbers between 1 and 50 in descending  order from 49 down to 1 using a while loop
i = 49

while i >= 1:
    print(i, end=" ")
    i -= 2

#11. Write a program that prints all multiples of 7 between 1 and 100.
i = 7

while i <= 100:
    print(i, end=" ")
    i += 7

#12. Write a program that continuously prompts the user to input numbers. The loop should terminate immediately when the user enters 0. Afterward, print the total sum of all numbers entered excluding the 0.
total = 0

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n

print(f"Total sum: {total}")

#13. Write a program that asks a user to enter their age. If the input is less than 0 or greater than 120, print invalid age and prompt them again. The loop should repeat until a valid age is provided.
while True:
    age = int(input("Enter your age: "))
    if 0 <= age <= 120:
        break
    print("Invalid age. Try again.")

print(f"Your age is {age}")

#14. Write a program that allows a teacher to input student scores one by one. The loop ends when the teacher types -1. The program should then calculate and display the average score
scores = []

while True:
    score = int(input("Enter score (-1 to stop): "))
    if score == -1:
        break
    scores.append(score)

average = sum(scores) / len(scores)
print(f"Average score: {average:.2f}")

#15. Write a program that simulates a login screen. Give the user a maximum of 3 attempts to type the correct password for example secret123. If they fail 3 times, print access denied, if they succeed early, print access granted and exit the loop.
password = "secret123"
attempts = 0

while attempts < 3:
    guess = input("Enter password: ")
    if guess == password:
        print("Access granted.")
        break
    attempts += 1
    print(f"Wrong password. {3 - attempts} attempt(s) remaining.")
else:
    print("Access denied.")

#16. Write a program that takes an integer input and constructs a new integer that is the exact reverse of the input for example input is 582 outputs the actual integer 285.
n = int(input("Enter an integer: "))

original = n
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

print(f"Reversed: {reversed_num}")

#17
n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1


#18
string = input("Enter a string: ")
result = ""
i = 0

while i < len(string):
    if string[i] not in "aeiouAEIOU":
        result += string[i]
    i += 1

print(f"Without vowels: {result}")

#19
string = input("Enter a string: ")
count = 0
i = 0

while i < len(string) - 1:
    if string[i:i+2] == "hi":
        count += 1
    i += 1

print(f"'hi' appears {count} times")


#20
numbers = [12, 25, 7, 30, 18, 40, 55, 9]
i = 0

while i < len(numbers):
    if numbers[i] % 5 == 0:
        print(numbers[i], end=" ")
    i += 1

#21
string = input("Enter a string: ")
result = ""
i = 0

while i < len(string):
    if string[i].islower():
        result += string[i].upper()
    elif string[i].isupper():
        result += string[i].lower()
    else:
        result += string[i]
    i += 1

print(f"Swapped: {result}")



#32
start = int(input("Enter start: "))
end = int(input("Enter end: "))

n = start
while n <= end:
    if n > 1:
        i = 2
        is_prime = True
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(n, end=" ")
    n += 1



#33
numbers = [12, 40, 21, 31, 10, 7, 5]

for n in numbers:
    if n < 20:
        print(n, end=" ")


#34
numbers = [45, 60, 12, 75, 30, 55, 8, 90]
i = 0

while i < len(numbers):
    if numbers[i] > 50:
        numbers[i] = 0
    i += 1

print(numbers)


#35
numbers = [15, 25, 30, 45, 60, 12, 90, 7]
count = 0

for n in numbers:
    if n % 3 == 0 and n % 5 == 0:
        count += 1

print(f"Count: {count}")


#36
numbers = [10, 15, 25, 30, 45]
i = 0
sorted = True

while i < len(numbers) - 1:
    if numbers[i] > numbers[i + 1]:
        sorted = False
        break
    i += 1

print("Sorted" if sorted else "Not Sorted")


#37
i = 97

while i <= 122:
    print(chr(i), end=" ")
    i += 1

#38
chapters = [45, 30, 50, 40]
i = 0

while i < len(chapters):
    print(f"Chapter {i + 1} has {chapters[i]} pages")
    i += 1


#39
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
i = 0

while i < len(list1):
    if list1[i] in list2:
        print(list1[i], end=" ")
    i += 1

#40
tables = [2, 4, 6, 7, 8]

for t in tables:
    print(f"\n--- Table of {t} ---")
    i = 1
    while i <= 10:
        print(f"{t} x {i} = {t * i}")
        i += 1

#41
numbers = [1, 2, 3, 2, 5]
seen = []
i = 0
has_duplicate = False

while i < len(numbers):
    if numbers[i] in seen:
        has_duplicate = True
        break
    seen.append(numbers[i])
    i += 1

print("Has Duplicates" if has_duplicate else "No Duplicates")