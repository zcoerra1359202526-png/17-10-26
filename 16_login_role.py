# User Role Message

role = input("Enter role (admin, student, guest): ").lower()

if role == "admin":
    print("Welcome, administrator")
elif role == "student":
    print("Welcome, student")
elif role == "guest":
    print("Welcome, guest")
else:
    print("Unknown role")
