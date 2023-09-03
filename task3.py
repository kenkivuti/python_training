# write a program which gets a phone number from a form input or terminal.
# validates the phone number by checking if it starts with +254.. or 07..
# or 71.. or 254.. 0r 01.. convert the number to start with +254...

# eg if user enters "0712345678", the program should display "+254712345678"

phonenumber = input("enter phone number : ")



if phonenumber.startswith("07") and len(phonenumber)== 10:
    number = "+254" + phonenumber[1:] 

elif phonenumber.startswith("01") and len(phonenumber)== 10:
    number = "+254" + phonenumber[1:]

elif phonenumber.startswith("254") and len(phonenumber)== 12:
    number = "+"+ phonenumber[0:]

elif phonenumber.startswith("1") and len(phonenumber)==9:
    number = "+254" + phonenumber[0:]

elif phonenumber.startswith("7") and len(phonenumber)==9:
    number = "+254" + phonenumber[0:]

elif phonenumber.startswith("+254") and len(phonenumber)==13:
    number = "" + phonenumber[0:]
    print(number)
else:
    print("not a phonenumber")








