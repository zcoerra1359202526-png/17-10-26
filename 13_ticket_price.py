# Ticket Price by Age

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 5:
    print("Ticket is free")
elif age < 18:
    print("Child ticket: Rs. 50")
elif age < 60:
    print("Adult ticket: Rs. 100")
else:
    print("Senior ticket: Rs. 60")
