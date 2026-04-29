#1 A hospital system stores patient names in random case for example rahUl DahaL.
name = "rahUl DahaL"
# Convert the name to title format on the prescription.
name = name.title()
print(name)
#2 A cybersecurity system requires all passwords to be checked in lowercase for consistency. Take a password input like 'Pass@123' and convert it for comparision.
password = 'Pass@123'
password = password.lower()
print(password)

#3 A movie ticket booking system receives the movie name in lowercase‘spider-man no way home’. Display it in title case on the ticket
movie_name = "spider-man no way home"
movie_name = movie_name.title()
print(movie_name)

#4 A school notice board program takes a heading input and displays it in ALL CAPS for attention. Take input ‘annual sports day’ and display it.
heading = "annual sports day"
heading = heading.upper()
print(heading)

#5 A fun CAPS-LOCK reversal tool takes the sentence ‘hELLO wORLD’ and swaps every letter's case. Write a program for this
sentence = "hELLO wORLD"
sentence = sentence.swapcase()
print(sentence)

#6  document editor wants to find the first position where the word ‘error’ appears in a log message: ‘System error detected, error code 404
log_message = "System error detected, error code 404"
error_position = log_message.find("error")
print(f"The word 'error' first appears at position: {error_position}")

#7 An email validation system checks whether an entered email ends with ‘@gmail.com’. Write a program to validate it
email = "user@gmail.com"
if email.endswith("@gmail.com"):
    print("Valid Gmail address.")
else:
    print("Invalid Gmail address.")

#8. A spam filter counts how many times the word ‘free’ appears in a message: ‘Get free stuff, free gifts and free coupons now!’.
message = "Get free stuff, free gifts and free coupons now!"
free_count = message.count("free")
print(f"The word 'free' appears {free_count} times in the message.")

#9. A URL checker verifies whether a website link starts with "https" forsecurity. Write a program for this.
url2 = "https://www.example.com"
if url2.startswith("https"):
    print("The URL is secure.")
else:
    print("The URL is not secure.")

#10. A resume scanner checks whether the keyword ‘Python’ is present in a resume text. Use the in operator.
resume_text = "Experienced in Python programming and data analysis."
if "Python" in resume_text:
    print("The keyword 'Python' is present in the resume.")

#11. A bank transaction log uses index() to find the exact position of the word ‘FAILED’ in the message ‘Transaction FAILED due to low balance’.
transaction_log = "Transaction FAILED due to low balance"
failed_position = transaction_log.index("FAILED")
print(f"The word 'FAILED' first appears at position: {failed_position}")

#12. A government office receives a file named ‘budget_report.pdf’. Write a Python program that checks whether the file is a PDF document or not using endswith() and directly print the result.
file_name = "budget_report.pdf"
if file_name.endswith(".pdf"):
    print("The file is a PDF document.")
else:
    print("The file is not a PDF document.")

#13. A telecom registration system receives a phone number ‘+977-9841123111’. Write a Python program that checks whether the phone number starts with the Nepal country code ‘+977’. Print the result directly.
phone_number = "+977-9841123111"
if phone_number.startswith("+977"):
    print("The phone number is a valid Nepal number.")
else:
    print("The phone number is not a valid Nepal number.")

#14. A cybersecurity system receives a url ‘https://www.moha.gov.np/’. Write a Python program that checks whether the URL belongs to agovernment website, print the result directly.
url3 = "https://www.moha.gov.np/"
if url3.endswith(".gov.np"):
    print("The URL belongs to a government website.")
else:
    print("The URL does not belong to a government website.")

#15. A customer feedback form receives input with extra spaces: ‘ Great service! ‘. Clean it before saving to the database.
feedback = " Great service! "
feedback = feedback.strip()
print(feedback)

#16. A chat application replaces all occurrences of a banned word ‘hate’ with ‘****’ in the message "I hate this, hate it completely".
message = "I hate this, hate it completely"
banned_word = "hate"
clean_message = message.replace(banned_word, "****")

print(clean_message)
#17. A file system receives filenames with leading slashes like ‘///student_records.pdf ‘. Remove the leading slashes.
filename = "///student_records.pdf "
filename = filename.lstrip("/")
print(filename)

#18. A web scraper fetches product prices as ‘Price: $120.33 ‘ with trailing spaces. Clean the right side using rstrip() and remove symbols too.
price = "Price: $120.33 "
price = price.rstrip()
price = price.replace("$", "")
print(price)

#19. A phone number formatter takes ‘+977 984-123-4567’ and removes all dashes - using replace() to store only digits format.
phone_number1 = "+977 984-123-4567"
formatted_number = phone_number1.replace("-", "")

#20. A CSV file contains student data as ‘Aarav,22,Kathmandu,ComputerScience’. Split it into individual fields and display each on a new line.
student_data = "Aarav,22,Kathmandu,ComputerScience"
fields = student_data.split(",")
for field in fields:
    print(field)

#21. A social media app stores hashtags as a ‘Python, Coding, Nepal, Tech’.Join them with # prefix to display as #Python #Coding #Nepal #Tech.
hashtags = "Python, Coding, Nepal, Tech"
hashtag_list = hashtags.split(", ")
for hashtag in hashtag_list:
    print(f"#{hashtag}")

#22. A train ticket system receives passenger names separated by commas: ‘Ram, Shyam, Hari, Sita’. Split and count the total number of passengers.
passenger_names = "Ram, Shyam, Hari, Sita"
passengers = passenger_names.split(", ")
print(f"Total passengers: {len(passengers)}")

#23. A sentence builder takes individual words [‘The’, ‘flight’, ‘departs’, ‘at’,‘6AM’] and joins them with a space to form a proper sentence.
words = ['The', 'flight', 'departs', 'at', '6AM']
sentence = " ".join(words) 
print(sentence)

#24. A government form validation checks whether the entered age contains only digits. Take input ‘25’ or ‘25abc’ and validate it.
age = input("Enter your age: ")
if age.isdigit():
    print("Valid age entered.")
else:
    print("Invalid age entered.")

#25. A username registration system checks that the username contains only letters and numbers, no special characters.
username2 = input("Enter a username: ")
if username2.isalnum():
    print("Valid username entered.")
else:
    print("Invalid username entered.")

#26. A name field validator in a school admission form checks that the student's name contains only alphabets (no digits).
student_name = input("Enter the student's name: ")
if student_name.isalpha():
    print("Valid student name entered.")
else:
    print("Invalid student name entered.")

#27. A PIN verification system checks whether the user's PIN is all uppercase letters for a code like ‘ASDF’.
pin = input("Enter your PIN: ")
if pin.isupper():
    print("Valid PIN entered.")
else:    print("Invalid PIN entered.")

#28. A blank field detector in a form checks whether the user entered only spaces.
user_input = input("Enter some text: ")
if user_input.isspace():
    print("Input is blank (only spaces).")