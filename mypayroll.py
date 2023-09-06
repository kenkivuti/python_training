class Payroll():
    basic_salary=0
    benefit=0

    def __init__(self,basic_salary,benefit):

        self.basic_salary = basic_salary
        self.benefit = benefit
        self.forgross_sallary()
        self.fornhif()
        self.fornssf()
        self.fornhdf()
        self.fortaxable_income()
        self.forpayee()
        self.fornet_salary()


    def forgross_sallary(self):
        self.gross_sallary= float(self.basic_salary) + float(self.benefit)

        print("your gross_sallary" ,self.gross_sallary)


    # nhif
    def  fornhif(self):
           if  self.gross_sallary > 0 and self.gross_sallary < 5999:
               self.nhif = 150
           elif self.gross_sallary >= 6000 and self.gross_sallary <= 7999:
                self.nhif = 300
           elif self.gross_sallary >= 8000 and self.gross_sallary <= 11999:
                self.nhif = 400 
           elif self.gross_sallary >= 12000 and self.gross_sallary <= 14999:
                self.nhif = 500
           elif self.gross_sallary >= 15000 and self.gross_sallary <= 19999:
                self.nhif= 600 
           elif self.gross_sallary >= 20000 and self.gross_sallary <= 24999:
               self.nhif = 750 
           elif self.gross_sallary >= 25000 and self.gross_sallary <= 29999:
                self.nhif = 850 
           elif self.gross_sallary >= 30000 and self.gross_sallary <= 34999:
                self.nhif = 900 
           elif self.gross_sallary >= 35000 and self.gross_sallary <= 39999:
                self.nhif = 950 
           elif self.gross_sallary >= 40000 and self.gross_sallary <= 44999:
                self.nhif = 1000 
           elif self.gross_sallary >= 45000 and self.gross_sallary <= 49999:
                self.nhif = 1100
           elif self.gross_sallary >= 50000 and self.gross_sallary <= 59999:
                self.nhif = 1200 
           elif self.gross_sallary >= 60000 and self.gross_sallary <= 69999:
                self.nhif = 1300 
           elif self.gross_sallary >= 70000 and self.gross_sallary <= 79999:
                self.nhif = 1400 
           elif self.gross_sallary >= 80000 and self.gross_sallary <= 89999:
                self.nhif = 1500 
           elif self.gross_sallary >= 90000 and self.gross_sallary <= 99999:
                self.nhif = 1600 
           elif self.gross_sallary >= 100000:
                self.nhif = 1700
           else:
                self.nhif = 0
          
           print("your nhif", self.nhif)

    # nssf
    
    def fornssf(self,rate=0.06):
     if self.gross_sallary < 18000:
      self.nssf = self.gross_sallary * rate
     else: 
        self.nssf = 18000 * rate
     

     print("your nssf :" , self.nssf)

# nhdf
    
    def fornhdf(self,rate=0.015):
      self.nhdf = self.gross_sallary * rate
      if self.nhdf<2500:
       self.nhdf = self.gross_sallary * rate
      else:
          self.nhdf=2500   

      print("your nhdf : " , self.nhdf)


# taxableincome
    def fortaxable_income(self):
      self.taxable_income = self.gross_sallary - (self.nssf + self.nhdf)
  
      print("your taxable income : " ,self.taxable_income)  
                
# payee

    def forpayee(self):
     if self.taxable_income > 0 and self.taxable_income <= 24000:
        self.payee = ((24000 * 0.1) - 2400)
     elif self.taxable_income > 24001 and self.taxable_income <= 32333:
        self.payee = ((self.taxable_income * 0.1) + (8333 * 0.25)- 2400)
     elif self.taxable_income > 32334 and self.taxable_income <= 500000 :
        self.payee = ((24000 * 0.01) +(8333 * 0.25) +((self.taxable_income - 32333) * 0.3)- 2400)

     elif self.taxable_income > 500001:
        self.payee =((24000 * 0.01) +(8333 * 0.25) +((self.taxable_income - 32333) * 0.35)- 2400)
     else:
        self.payee = 0

     print("your payee",self.payee)
    

# netsalary

    def fornet_salary(self):
      self.net_salary = self.gross_sallary - (self.nhif + self.nhdf + self.nssf + self.payee)
  
      print("your net_salary : " , self.net_salary)


calcgross= Payroll(input("enter your basic_salary : "),
                    input("enter your benefit : "))