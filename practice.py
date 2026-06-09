
#User login system in 3 attempts
id = [{'username': 'Admin', 'password': '123456'},{'username': 'User', 'password': '654321'}]
for i in range(3):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in id:
        if user['username'] == username and user['password'] == password:
            print("Login successful!")
            break
    else:
         print("Access Denied")
         retries_remaining = 2 - i
         if retries_remaining > 0:
          print(f"You have {2-i} attempts left.")
         else:
            print("You have exceeded the maximum number of attempts. Please try again later.")
          
    
            
        
    

    
        

        
        

    

    
    