# Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 


num1 = float(input("enter a number1 : "))
num2 = float(input("enter a number2 : "))
num3 = float(input("enter a number3 : "))

if num1>num2 and num1>num3:
    print(num1,"num1 the largest")
elif num2>num1 and num2>num3:
    print(num2,"num2 is the largest")
else:
    print(num3,"num3 is the largest")