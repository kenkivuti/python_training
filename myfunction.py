# function - a block of reusable code.
# place()after the function name to invoke it 
def display_invoice(username,amount,due_date):
    print(f"hello {username}")
    print(f"your bill of ${amount:.2f}is due : {due_date}")

display_invoice("ken",50.0,"28/02/2024")


# return - statement used to end a function and send a result back to the caller. 

def add(x,y):
    z = x + y
    return z 


print(add(1,2))


gb = "tv"