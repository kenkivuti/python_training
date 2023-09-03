# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....


content = int(input("enter rows : "))
count=0
for i in range(1, content + 1):
    value=("*" * i)
    count=count+1
    if count==content:
        value=(value+("."*5))
    print(value)
