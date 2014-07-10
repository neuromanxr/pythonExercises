number = eval(input("Enter four digit number: "))
#print(int(number / 1))
#print(int(number / 10))
#print(int(number / 100))
#print(int(number / 1000))

fourth = (int(number % 1))
third = (int(number % 10))
second = (int(number % 100))
first = (int(number % 1000))

print("-------")

print(third)
print(int(second / 10))
print(int(first / 100))
print(int(number / 1000))
