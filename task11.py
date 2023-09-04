# Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.

from datetime import datetime

today = datetime.now()

dob = input("enter DOB (DD/MM/YYYY) : ")
sdob = dob.split("/")

if len(sdob) != 3 or int(sdob[0])<0 or int(sdob[0]) > 31 \
   or int(sdob[1])<0 or int(sdob[1]) > 12 or int(sdob[2]) < 1900 \
   or int(sdob[2]) > 2023:
    print("wrong date format")

else:
    y = today.year - int(sdob[2])
    m = today.month - int(sdob[1])
    d = today.day - int(sdob[0])

    if d < 0 :
        m = m-1
        d = d + 31
    else:
        pass

    if m < 0 :
        y = y-1
        m = m + 12

    print(str(d) , "-",str(m),"-" ,str(y))
