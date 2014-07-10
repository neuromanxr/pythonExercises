import random
import time

#print(number1, number2)

NUMBEROFQUE = 5
contLoop = 'y'

countRight = 0
countWrong = 0

startTime = time.time()

count = 0
while contLoop == 'y': #count < NUMBEROFQUE:
    number1 = random.randrange(0, 9)
    number2 = random.randrange(0, 9)

    if number1 < number2: number1, number2 = number2, number1
    print("Evaluate: ", str(number1), "-", str(number2))
    answer = eval(input())
    if answer == number1 - number2:
        print("Right")
        #count = count + 1
        countRight = countRight + 1
    else:
        print("Wrong")
        countWrong = countWrong + 1
    count = count + 1
    contLoop = input("Continue?")

endTime = time.time()
testTime = int(endTime - startTime) 
print("Right: ", countRight)
print("Wrong: ", countWrong)
print("Your time: ", testTime, "seconds")


