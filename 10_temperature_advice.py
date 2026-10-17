# Temperature Advice

temperature = float(input("Enter temperature in Celsius: "))

if temperature < 10:
    print("It is cold")
elif temperature < 25:
    print("The weather is mild")
elif temperature < 35:
    print("It is warm")
else:
    print("It is very hot")
