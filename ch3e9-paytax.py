employeeName = input("Enter name: ")
hoursWorked = eval(input("Enter hours worked: "))
hourlyPayRate = eval(input("Enter hourly pay rate: "))
fedTax = eval(input("Enter federal tax rate: "))
stateTax = eval(input("Enter state tax rate: "))

grossPay = hoursWorked * hourlyPayRate
fedTaxPay = fedTax * grossPay
stateTaxPay = stateTax * grossPay
totalDeduct = fedTaxPay + stateTaxPay
netPay = grossPay - totalDeduct

print("-----------")
print(employeeName)
print("Hours Worked: ", format(hoursWorked, ".1f"))
print("Pay Rate: ", "$", format(hourlyPayRate, ".2f"))
print("Gross Pay: ", "$", format(grossPay, ".2f"))
print("Deductions---")
print(" Federal Withholding ", "(",format(fedTax, ".1%"),")", \
      "$", format(fedTaxPay, ".2f"))
print(" State Withholding ", "(",format(stateTax, ".1%"),")", \
      "$", format(stateTaxPay, ".2f"))
print(" Total Deductions: ", "$", format(totalDeduct, ".2f"))
print("Net Pay: ", "$", format(netPay, ".2f"))
