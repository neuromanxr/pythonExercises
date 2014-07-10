moneyAmount = eval(input("Enter dollars and cents: "))
moneyAmount = round(moneyAmount, 2)
moneyAmount = moneyAmount * 100
moneyDollars = moneyAmount / 100
moneyCents = round((moneyAmount % 100), 2)
moneyQuarters = moneyCents / 25
moneyRemainCents1 = moneyCents % 25
moneyDimes = moneyRemainCents1 / 10
moneyRemainCents2 = moneyRemainCents1 % 10
moneyNickels = moneyRemainCents2 / 5
moneyRemainCents3 = moneyRemainCents2 % 5
moneyPennies = moneyRemainCents3 / 1

#print(int(moneyAmount))
print("\t",int(moneyDollars),"dollars")
#print(int(moneyCents),"cents")
print("\t",int(moneyQuarters),"quarters")
#print(int(moneyRemainCents1),"cents")
print("\t",int(moneyDimes),"dimes")
#print(int(moneyRemainCents2),"cents")
print("\t",int(moneyNickels),"nickels")
print("\t",int(moneyPennies),"Pennies")


