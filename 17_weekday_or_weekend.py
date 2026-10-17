# Day of the Week

day = input("Enter a day: ").strip().lower()

if day in ("saturday", "sunday"):
    print("Weekend")
elif day in ("monday", "tuesday", "wednesday", "thursday", "friday"):
    print("Weekday")
else:
    print("Invalid day")
