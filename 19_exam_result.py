# Exam Result Checker

marks = float(input("Enter marks out of 100: "))
attendance = input("Is attendance approved? (yes/no): ").lower()

if marks < 0 or marks > 100:
    print("Invalid marks")
elif attendance != "yes":
    print("Check attendance requirement")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
