import random

number = random.randrange(0, 10)

even = number % 2 == 0

if even:
    even = True
else:
    even = False

print(number)
print(even)


count = random.randrange(0, 10)
newLine = count % 10 == 0

if newLine:
    newLine = True
else:
    newLine = False

number = eval(input("Enter number: "))

if number % 2 == 0:
    print(number, "is even")
elif number % 5 == 0:
    print(number, "is multiple of 5")
