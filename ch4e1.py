a, b, c = eval(input("Enter a, b, c: "))

Discr1 = (b ** 2 - 4 * a * c)
Discr2 = Discr1

root1 = (-1 * b + Discr1 ** 0.5) / 2 * a
root2 = (-1 * b - Discr2 ** 0.5) / 2 * a

if Discr1 > 0:
    print("Root 1 is: ", root1, "Root 2 is: ", root2)
elif Discr1 == 0:
    print("Root is: ", root1)
else:
    print("No real roots")

#print(root1, ",", root2)
