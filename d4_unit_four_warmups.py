age = int(input("What is your age?"))
if age <= 2:
    print("Your ticket is free!")
elif age >= 3 and age <= 12:
    print("Your ticket cost $8")
else:
    print("Your ticket cost $10")
