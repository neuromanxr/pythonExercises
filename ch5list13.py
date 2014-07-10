

#primeCount = 0
#count = 0
    
##userInput = eval(input("Enter number: "))
##if userInput % 1 == 0 and \
##   userInput % userInput == 0:
##    for count in range(1, userInput):
##        count += 1
##        if userInput % count != 0:
##            print("prime")
##        else:
##            print("not prime")
temp = 0
primeCount = 0
numberOfPrimes = 50
number = 1
#number = eval(input("Enter number: "))
#for number in range(1, 51):
while primeCount < numberOfPrimes:
    number += 1
    for count in range(1,number + 1):
        result = number % count
        if result == 0:
            temp += 1
        #print(result)
        count += 1
    #print(":::", temp)
    if temp == 2:
        primeCount += 1
        print(number, "prime")
    #else:
    #    print(number, "not prime")
    temp = 0

    
