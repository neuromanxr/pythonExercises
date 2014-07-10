income = eval(input("Enter income: "))

if income <= 10000:
    tax = income * 0.1
elif income <= 20000:
    tax = 1000 + (income - 10000) * 0.15

print(tax)


if income <= 10000:
    tax = income * 0.1
elif income > 10000 and income <= 20000:
    tax = 1000 + (income - 10000) * 0.15

print(tax)
