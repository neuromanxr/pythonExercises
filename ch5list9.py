year = 0

tuition = 69000
finalTuition = tuition * 2
#tuition = tuition * 1.07

while tuition < finalTuition:
    tuition = (tuition * 1.03)
    year += 1
    print("Year: ", year, "Tuition: ", format(tuition, ".2f"))

print("The tuition will be " + str(format(tuition, ".2f")) + " at year " + str(year))
