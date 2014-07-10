def primeNumber(number):
    divisor = 2
    #number = number / 2
    while divisor <= number / 2:
        #print("Number", number)
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def printPrime():
    count = 0
    PRIMES = 2
    numberOfPrimes = 100000
    primesPerLine = 10
    while count <= numberOfPrimes:
        PRIMES += 1
        #primeNumber(numberOfPrimes)
        if primeNumber(PRIMES):
            print(PRIMES, end = ' ')
            if count % primesPerLine == 0:
                print()
            count += 1

printPrime()
                       
