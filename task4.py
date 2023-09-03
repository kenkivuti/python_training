# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.

mail = input("enter your email : ")

if mail.endswith(".") and "@" not in mail  or "." not in mail or mail.count("@")>1 and mail.index(".")>mail.index("@"+1):
    print("invalid email")

elif mail.index("@")> 0 and mail.index(".") > 2 :
    print("valid email")

else:
    pass


# email = input("Enter your email adress: ")
# valid=""
# if email.index("@")>1 and (email.index(".")<len(email)-1) and (email.index(".")>email.index("@")):
#     valid=(f"{email} is a valid email")
# else:
#     valid=(f"{email} is not a valid email")
# print(valid)