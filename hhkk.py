schaddr="my school, \n123 main st,\nTimbutku, OH 43500"
#my school, \n123 main st,\nTimbutku, OH 43500")
print ("My Schools address is : \n")
print (schaddr)


hometown=input("Enter your hometown::")
print(hometown*3)
#print(hometown)

age=input("Your age please:")
#print(type(age))
age=int(age)
if age < 5:
    print("Diaper time")
elif age >5 and age < 35:
    print("MineCraft age")
elif age > 35 and age <= 50:
    print("Go play soccer")
else:
    print("Happy retirement")