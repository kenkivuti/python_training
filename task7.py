# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


marks = float(input("enter your marks : "))

if marks >= 79 and marks <= 100:
    marks = "A"
elif marks >= 60 and marks < 79:
    marks = "B"
elif marks >= 49 and  marks < 60:
    marks = "C"
elif marks >= 40 and marks < 49:
    marks = "D"
elif marks > 0 and marks < 40:
    marks = "E"
else:
    print("invalid marks")

print(marks)