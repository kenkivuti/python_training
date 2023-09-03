# given a variable temperature with a value of 25c, write an if statement to check if the temperature
# is above  30c using the greater than (>) operator.

temp = 25

if temp >= 0 and temp <= 30:
        print("temperature is good")
else:
        print("temperature is bad")

#  create a dictionary called stock with items as keys and their quantities as values.
# write an if-else statement to check if the quantities of "apples" is zero using the 
# equality(==)operator

stocks = {
        "apple": 40,
        "orange": 10,
        "banana": 30,

}
if stocks["apple"] == 0:
        print("quantity is zero")
else:
        print("greater than zero")


# Declare a list called even_numbers containing integers.
#  Write an if statement to check if the first element of the list is an even number using the modulo (%) operator
even_numbers = [10,4,5,6,7,9,2,3]
if even_numbers[0] % 2 == 0 :
        print("even number")







# Imagine you have a list employees containing dictionaries with keys "name", "hours_worked", and "hourly_rate". 
# Write a code snippet using nested if statements to calculate the salary for an employee named "Alice" 
# based on her hours worked and hourly rate.

employees = [{"name":"ken",
                 "hours_worked":20,
                 "hourly_rate": 10,
              },
                { "name":"alice",
                 "hours_worked":22,
                 "hourly_rate": 15,
                }
                 ]

if employees[1]["name"] == "alice" :
        print("she is in ")
else :
        print("she is not")


# Create a dictionary book_ratings with book titles as keys and their ratings as values.
#  Write an if-elif-else statement to find out if a book "The Adventure" has a rating of 5 or is rated below 2.

book_ratings = {
        "playlist" : 3,
        "the adventure" : 5,
        "top 10" : 2
}
if book_ratings["the adventure"] == 5:
        print("it has a rating of 5")
else:
        print("rating is below 2")

# 	Suppose you have two sets: set_x and set_y.
#  Write a code snippet using conditional statements to check if the symmetric difference between the two sets is not empty,
#  using the ^ (symmetric difference) operator

set_x = {"ken",5,4,2}
set_y = {"ken","joe","max"}

if set_x^set_y:
        symetric=set_x^set_y
else:
        symetric="none"
print(symetric)