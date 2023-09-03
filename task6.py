# Write a program input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. 
# If the password is correct access is granted. After you show them a message , the account is blocked.

password = "admin@123"

for i in range(0,4):
    enter_password = (input("enter your password : "))
    if enter_password==password:
        print("password is valid")
        break
else:
    enter_password==i
    print("blocked")