# Temperature Range Demo

temperature = float(input("Enter a temperature in Celsius: "))

if temperature < 35:
    print("Below the typical human body temperature range")
elif temperature <= 37.5:
    print("Within a common body-temperature range")
else:
    print("Above a common body-temperature range")

print("This is a simple educational example, not a diagnosis.")
