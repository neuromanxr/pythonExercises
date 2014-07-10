weight = eval(input("Enter weight in lbs: "))
height = eval(input("Enter height in inches: "))

lbsToKilo = weight * 0.45359237
inchesToMeters = height * 0.0254

bmi = lbsToKilo / (inchesToMeters ** 2)

print(bmi)
