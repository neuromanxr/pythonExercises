##Sum = 0
##number = 0
##
##while number < 20:
##    number += 1
##    #sum += number
##    if number == 10 or number == 11:
##        continue
##    Sum += number
##
###print("Number is: ", number)
##print("The sum is: ", Sum)
##
##
##number = eval(input("enter number: "))
##factor = 2
##while factor < number:
##    if number % factor == 0:
##        break
##    factor += 1
##
##print("Smallest factor other than 1 for", number, "is", factor)
##
##
##balance = 1000
##while True:
##    if balance < 9:
##        break
##    balance = balance - 9
##    #print(balance)
##
##print("Balance is", balance)
##
##Sum = 0
##for i in range(4):
##    if i % 3 == 0:
##        continue
##    Sum += i
##
##print(Sum)
##print(i)
##
##print("-------------")
##
##Sum = 0
##i = 0
##while i < 4:
##    i += 1
##    if i % 3 == 0:
##        break
##    Sum += i    
##
##print(Sum)
##print(i)

##sum = 0
##number = 0
##
##while number < 20:
##    number += 1
##    if number == 10 or number == 11:
##        continue
##    sum += number
##
##print("The sum is", sum)
##
##print("-------------")
##
##sum = 0
##number = 0
##
##while number < 20:
##    number += 1
##    if number == 10 or number == 11:
##        sum += 0
##    else:
##        sum += number
##
##print("The sum is", sum)

##sum = 0
##number = 0
##
##while number < 20:
##    number += 1
##    sum += number
##    if sum >= 100:
##        break
##print("The number is", number)
##print("The sum is", sum)
##
##print("-------------")
##
##sum = 0
##number = 0
##stop = True
##
##while number < 20 and stop == True:
##    number += 1
##    sum += number
##    if sum >= 100:
##        stop = False
##
##
##print("The number is", number)
##print("The sum is", sum)

for i in range(1, 4):
    for j in range(1, 4):
        if i * j > 2:
            break
        print(i * j)
    print(i)
