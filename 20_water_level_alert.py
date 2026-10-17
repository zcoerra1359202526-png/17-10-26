# Water Tank Level Alert

level = float(input("Enter tank level percentage (0-100): "))

if level < 0 or level > 100:
    print("Invalid level")
elif level < 20:
    print("Alert: Water level is low")
elif level < 80:
    print("Water level is normal")
else:
    print("Warning: Tank is nearly full")
