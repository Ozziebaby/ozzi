number =int(input("enter a number:  "))
r3= number % 3
r5 = number % 5
if r3 == 0 and r5 == 0:
    print("number is a multiple of both 3 and 5")
elif  r3 == 0:
    print("number is a multple of 3")
elif r5 == 0:
    print("number is a multiple of 5")
else:
    print("match not found")
