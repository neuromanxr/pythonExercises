import random

number1 = random.randrange(0, 9)
number2 = random.randrange(0, 9)

if number1 > number2:
    op1 = number1 - number2
    print(number1, "-", number2, "=")
    answer = eval(input(""))
    while answer != op1:
        print("wrong try again")
        answer = eval(input(""))
    if op1 == answer:
        print("correct")

else:
    op2 = number2 - number1
    print(number2, "-", number1, "=")
    answer = eval(input(""))
    while answer != op2:
        print("wrong try again")
        answer = eval(input(""))
    if op2 == answer:
        print("correct")




