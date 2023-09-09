blogs = [{"id":1,"title":"PCI","description":"starting..","status":0},
         {"id":2,"title":"TSI","description":"starting..","status":0},
         {"id":3,"title":"VWS","description":"starting..","status":1},
         {"id":4,"title":"ABC","description":"starting..","status":0},
         {"id":5,"title":"JKI","description":"starting..","status":1}]


# filter in the list only active blogs and change tittle to tittle case.
# use only maps and comprehensions
lsc = [blog for blog in blogs if blog["status"]==1 ]
 
def change_case(x):
    w=x["title"].title()
    x["title"]=w
    return x

result= list(map(change_case,lsc))

print(result)


# x = map(myfunc, ('apple', 'banana', 'cherry'))