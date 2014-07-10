# Prompt
purchaseAmount = eval(input("Enter purchase amount: "))
TAX = 0.0888
salesTax = purchaseAmount * TAX
salesTax = round(salesTax * 100) / 100.0
totalAmount = purchaseAmount + salesTax

print(salesTax)
print(totalAmount)
