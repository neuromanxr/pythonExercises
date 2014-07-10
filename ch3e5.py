# Prompt
import math

#PI = 3.14159
numberOfSides = eval(input("Enter number of sides: "))
sideLength = eval(input("Enter length of side: "))

area = numberOfSides * sideLength ** 2 / \
       (4 * math.tan(math.pi / numberOfSides))

print(area)
print(format(area, ".2f"))
