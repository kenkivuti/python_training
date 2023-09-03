# Write a program that takes input of someone's basic salary and benefits, 
# adds them to find the gross salary then uses  the gross salary to find the NHIF. 

basic_salary = float(input("enter your basicsalary : "))
benefits = float(input("enter your benefits : "))

gross_salary = basic_salary + benefits

print( "your gross_salary :" , gross_salary)

nhif = 0
if  gross_salary > 0 and gross_salary < 5999:
     nhif = 150
elif gross_salary >= 6000 and gross_salary <= 7999:
     nhif = 300
elif gross_salary >= 8000 and gross_salary <= 11999:
     nhif = 400 
elif gross_salary >= 12000 and gross_salary <= 14999:
     nhif = 500
elif gross_salary >= 15000 and gross_salary <= 19999:
     nhif = 600 
elif gross_salary >= 20000 and gross_salary <= 24999:
     nhif = 750 
elif gross_salary >= 25000 and gross_salary <= 29999:
     nhif = 850 
elif gross_salary >= 30000 and gross_salary <= 34999:
     nhif = 900 
elif gross_salary >= 35000 and gross_salary <= 39999:
     nhif = 950 
elif gross_salary >= 40000 and gross_salary <= 44999:
     nhif = 1000 
elif gross_salary >= 45000 and gross_salary <= 49999:
     nhif = 1100
elif gross_salary >= 50000 and gross_salary <= 59999:
     nhif = 1200 
elif gross_salary >= 60000 and gross_salary <= 69999:
     nhif = 1300 
elif gross_salary >= 70000 and gross_salary <= 79999:
     nhif = 1400 
elif gross_salary >= 80000 and gross_salary <= 89999:
     nhif = 1500 
elif gross_salary >= 90000 and gross_salary <= 99999:
     nhif = 1600 
elif gross_salary >= 100000:
     nhif = 1750
else:
    nhif = 0

print("your nhif : " , nhif)



# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate using. Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 


if gross_salary < 18000:
 nssf = gross_salary * 0.06
        
else: 
        nssf = 18000 * 0.06
        
print("your nssf :" , nssf)


# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

nhdf = gross_salary * 0.015

print("your nhdf : " , nhdf)
      

# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF) 

taxable_income = gross_salary - (nssf - nhdf)
print("your taxable income : " , taxable_income)


# Continue with the same program and find the person's PAYEE using the taxable income above.

payee = 0
if taxable_income > 0 and taxable_income <= 24000:
    payee = ((24000 * 0.1) - 2400)
elif taxable_income > 24001 and taxable_income <= 32333:
  payee = ((taxable_income * 0.1) + (8333 * 0.25)- 2400)
elif taxable_income > 32334 and taxable_income <= 500000 :
  payee = ((24000 * 0.01) +(8333 * 0.25) +((taxable_income - 32333) * 0.3)- 2400)

elif taxable_income > 500001:
  payee =((24000 * 0.01) +(8333 * 0.25) +((taxable_income - 32333) * 0.35)- 2400)
else:
  payee = 0

print ( "your payee : " ,payee)


# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

net_salary = gross_salary - (nhif + nhdf + nssf + payee)
print("your net_salary : " , net_salary)