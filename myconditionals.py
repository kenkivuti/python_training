# comparison:
# equal ; ==
# not equal ; !=
#  greater than ; .
# less than ; <
# greater or equal ; >=
#  less or equal ; <=
# object identity ; is

#  if statements
# 1
language = "python"
if language == "python":
    print("language is python")
elif language == "java":
    print("language is java")
else:
    print("no match")

#  2
x = 5
y = 10
z = 22

if x > y:
    print("x is greater than y")
elif x < z :
    print("x is less than z")
else:
    print("if and elif never ran")

#Take user input and ask them for their marks. Print their grade.
average_marks= 70
if average_marks  >= 70:
 		 print("A")
elif average_marks  >= 60 and average_marks  < 70:
 	 print("B")
elif average_marks  >= 50 and average_marks  < 60:
   		print("C")
elif average_marks  >= 40 and average_marks  < 50:
   		print("D")
else:
   print("E")

#    write a program to check wether a number is divisible by 7 

# the_number = int(input("enter number : "))

# if the_number % 7 == 0:
#         print("divisible")
# else:
#         print("not divisible")


# write a program to calculate the electricity bill based on following criteria.
# unit
# first 50 units - kshs.20
# next 50 units - kshs.40
# after 100 units - ksh.100

electricity_bill = int(input("enter your units : "))

if electricity_bill > 0 and electricity_bill <= 50 :
        print(electricity_bill*20, "ksh")
elif electricity_bill > 50 and electricity_bill <= 100 :
        print(((electricity_bill-50)*40) + 1000,"kshs")
else:
        print(((electricity_bill-100)*100)+ 3000,"kshs")
