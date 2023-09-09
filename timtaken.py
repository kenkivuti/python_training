import time

st=time.time()
for i in range(10000):
    pass
et=time.time()
el=et - st

st2 = time.time()
for i in range(10000000):
    pass
et2 = time.time()

el2= et2 - st2

print(el)
print(el2)


# starttym=time.time()

# for i in range (0,10000000):
#     endtym=time.time()
#     finaltym=endtym - starttym





lst = [2,98,10,3,6,4,0]

for i in range (0,len(lst)):

    for k in range(i+1,len(lst)):
        if lst[i] > lst[k]:
            lst[k],lst[i]=lst[i],lst[k]
            pass

print(lst)

# generate numbers between 1,000 and 10,000 and write only the numbers divisible by 7 in a .txt file