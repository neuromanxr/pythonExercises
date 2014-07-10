
gcd = 1

number1 = eval(input("enter first number: "))
number2 = eval(input("enter second number: "))

k = 1

while k <= number1 and k <= number2: #for k in range(2, number1 and number2):
    if number1 % k/2 == 0 and number2 % k/2 == 0:
        gcd = k
    k += 1
    
print(gcd)


gcd = 1
k = 1

number1 = eval(input("enter first number: "))
number2 = eval(input("enter second number: "))

if number1 > number2:
    numbmax = number1
else:
    numbmax = number2

for k in range(1, numbmax):
    if number1 % k == 0 and number2 % k == 0:
        gcd = k
    k += 1
print(gcd)
