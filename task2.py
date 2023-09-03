# prompt the user for a number either on a form input or the terminal.
# depending on whether the number is even or odd,display either "odd"
# or "even" to the user.


number = int(input("enter a number : "))

if number % 2 == 0 :
    print("even")
if number % 4 == 0:
    print("divisible by 4")
else:
    print("odd")
