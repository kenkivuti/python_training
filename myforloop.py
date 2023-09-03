i = [3,8,7,4,9,2]
for x in i:
    print(x)

# write a for loop to print numbers from 1 to 5
for x in range(1,5):
    print(x)

# sum all the elements in a list using a for loop 

numbers = [2,3,4,5,6,7,8,9]
total=0
for i in numbers:
    total += i
print(total)


ls = list(range(20,61))

res = []
for i in ls:
    # if i%7==0:
        res.append(i)
    # else:       
    #  pass
print(ls)


# store only the first 10 odd numbers between 0 and 50.

odd_numbers = list(range(0,51))

first_odd = []

for i in odd_numbers:
      if len(first_odd)==10:
              break
      elif i%2 != 0:
            first_odd.append(i)
           
      else:
          pass
print(first_odd)


accnt = 0
for i in range(0,51):
      if i%2 != 0 :
         print(i)

         accnt = accnt + 1
      elif accnt == 10:
           break
      else:
           pass
           
                     