#Prompt
finalAmount = eval(input("Enter final amount: "))
annualInterest = eval(input("Enter annual interest rate: "))
monthlyInterest = annualInterest / 1200
years = eval(input("Enter years: "))


initialAmount = finalAmount / ((1 + monthlyInterest) ** (years * 12))

print(round(initialAmount, 2))
