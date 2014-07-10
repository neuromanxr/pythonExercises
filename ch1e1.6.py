annualInterestRate = eval(input("Enter annual interest rate in percentage: "))
monthlyInterestRate = annualInterestRate / 1200

numberOfYears = eval(input("Enter number of years: "))
loanAmount = eval(input("Enter loan amount: "))

monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / \
    (1 + monthlyInterestRate) ** (numberOfYears * 12))
totalPayment = monthlyPayment * 12 * numberOfYears


print("Monthly payment is: ", round(monthlyPayment, 2))
print("Total payment is: ", round(totalPayment, 2))
