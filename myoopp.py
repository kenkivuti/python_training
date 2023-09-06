
# classes are collection of function and variables
# that are relatable and can manipulate each other.
# a function inside a class is caalled a method.
# a variable inside a class is called a property
# representation of of something in real world
# e.g student
# here you have all functions and properties
# related to student e.g create_student() , email
# ERP


# class person :
#     def __init__(self) :
#         self.name = "sam"
#         self.gender = "Male"
#         self.age = 18

#     def talk(self):
#             print("hi i am ",self.name)

#     def vote(self):
#             if self.age < 18:
#                 print("i am not eligible to vote") 
#             else:
#                 print("i am eligible to vote")

# obj = person()
# person.talk(obj)
# person.vote(obj)


# x=0
# def myincreament():
#     print("X0 is" ,x)
#     x=x+1

# myincreament()
# print("X1 is",x) 
# constructor - a special method used to  instantiate initial values

class Person():
    name = ""
    gender = ""
    email = ""
    phone = ""
    details =[]

    def __init__(self,n,g,e,p) :
        self.name = n
        self.gender = g
        self.email = e
        self.phone = p
        self.add()

    def add (self):
        self.details.append(self.name)
        self.details.append(self.gender)
        self.details.append(self.email)
        self.details.append(self.phone)


p1 = Person(input("enter name"),
            input("enter gender"),
            input("enter email"),
            input("enter phonenumber"))


p1.add()
print(p1.details)


