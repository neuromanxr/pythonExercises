print("        Mult Table")

print("   |", end = '')
for j in range(1, 10):
    print("  ", j, end = '')
print()
print("-------------------")

for i in range(1, 10):
    print(i, "|", end = '')
    for j in range(1, 10):
        print(format(i * j, "4d"), end = '')
    print()


for i in range(1, 5):
    j = 0
    while j < i:
        print(j, end = " ")
        j += 1

i = 0
while i < 5:
    for j in range(i, 1, -1):
        print(j, end = " ")
    print("****")
    i += 1

i = 5
while i >= 1:
    num = 1
    for j in range(1, i + 1):
        print(num, end = "xx")
        num *= 2
    print()
    i -= 1

i = 1
while i <= 5:
    num = 1
    for j in range(1, i + 1):
        print(num, end = "G")
        num += 2
    print()
    i += 1

count = 0
i = 0.01
Sum = 0
while count <= 100:
    Sum += i
    i = i + 0.01
    count += 1

print("The sum is", Sum)

Sum = 0
i = 0.01
for count in range(100):
    Sum += i
    i = i + 0.01

print("The sum is", Sum)
