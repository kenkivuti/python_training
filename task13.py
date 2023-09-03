# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com”
#  and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.

mail ="admin@mail.com"
password ="Admin@123"

enter_mail = input("enter your email : ")
enter_password = input("enter your password : ")

if enter_mail == mail and enter_password == password :
    print("login successful")
else:
    print("invalid username or password")
