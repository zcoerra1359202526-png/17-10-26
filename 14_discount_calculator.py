# Shopping Discount

amount = float(input("Enter shopping amount in Rs.: "))

if amount < 0:
    print("Invalid amount")
elif amount >= 5000:
    discount = 0.20
elif amount >= 2000:
    discount = 0.10
elif amount >= 1000:
    discount = 0.05
else:
    discount = 0

final_amount = amount * (1 - discount)
print("Discount:", discount * 100, "%")
print("Final amount: Rs.", round(final_amount, 2))
