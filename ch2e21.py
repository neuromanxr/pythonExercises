# Prompt
savingAmount = eval(input("Enter savings amount: "))
INTERESTRATE = 0.05
monthlyInterest = INTERESTRATE / 12
monthlyIntMult = 1 + monthlyInterest

firstMonth = savingAmount * monthlyIntMult
secondMonth = (firstMonth + savingAmount) * monthlyIntMult
thirdMonth = (secondMonth + savingAmount) * monthlyIntMult
fourthMonth = (thirdMonth + savingAmount) * monthlyIntMult
fifthMonth = (fourthMonth + savingAmount) * monthlyIntMult
sixthMonth = (fifthMonth + savingAmount) * monthlyIntMult


print(round(firstMonth, 2))
print(round(secondMonth, 2))
print(round(thirdMonth, 2))
print(round(fourthMonth, 2))
print(round(fifthMonth, 2))
print(round(sixthMonth, 2))
