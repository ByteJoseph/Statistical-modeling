#Write a program to confirm the validity of an email id by verifying its format
import re
form = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
email = str(input("Enter the email: "))
if re.match(form,email) is not None:
    print("correct")
else:
    print("incorrect")