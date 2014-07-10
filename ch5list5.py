


data = eval(input("Enter number (Input ends " + \
                  "if it is 0): "))

sum = 0
while data != 0:
    sum += data

    data = eval(input("Enter number (Input ends " + \
                      "if it is 0): "))

print("The sum is", sum)

i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
    i += 1

number = eval(input("Enter integer: "))
max = number

while number != 0:
    number = eval(input("Enter an integer: "))
    if number > max:
        max = number

    print("max is", max)
    print("number is", number)

for i in range(0, 10):
    print("number")
    #i = i + 1

number = 0
Sum = 0

for count in range(5):
    number = eval(input("Enter integer: "))
    Sum += number

print("sum is", Sum)
print("count is", count)

Sum = 0
for i in range(1001):
    Sum = Sum + i
print(Sum)
print(i)

Sum = 0
i = 0
while i < 1001:
    Sum = Sum + i
    i += 1
print(Sum)
print(i)

i = 1
for Sum in range(10000):
    Sum = Sum + i
    i += 1

print(Sum)
print(i)
