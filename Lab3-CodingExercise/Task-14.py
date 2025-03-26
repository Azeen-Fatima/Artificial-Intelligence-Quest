import re
password = input("Enter your password: ")
if(6<=len(password)<=16 and 
   re.search("[a-z]",password) and 
   re.search("[A-Z]",password) and 
   re.search("[0-9]",password) and
   re.search("[@$#]",password)):
    print("Valid password")
else:
    print("Invalid password")