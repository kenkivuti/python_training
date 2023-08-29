trainees = ["John", [2, ["James","Mary"]]]
# display 2 using index
# print(trainees[1][0])

# add 56 at the end of the list
trainees.append(56)
print(trainees)

# Output James  from the list.
print(trainees[0])

# Using a method add the name Mike between James and Mary
trainees[1][1].insert(1,"mike")
print(trainees)

# Change the value of 2 to 8
trainees[1][0]=8
print(trainees)

# Remove John and Mary from the list.
del trainees[1][1][2]
print(trainees)









# cars = ["volvo" , "ford",["toyota" , "mercedes" ,["mazda" ,"subaru"]],"audi"]
# cars.pop()
# cars.clear()
# model = ["suv","minivan","sedan"]
# owners = ["allan","ken","ivy"]

# cars.extend(model),cars.extend(owners)
# print(cars)

# cars[2][2].insert(1,"isuzu")
# print(cars)

# car1 = input("enter car name :")
# car2 = input("enter car name :")
# car3 = input("enter car name :")

# model = []
# model.append(car1),model.append(car2),model.append(car3)
# model.remove("bmw")
# del()
# print(car1,car2,car3)
# print(model)

