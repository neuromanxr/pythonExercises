def FizzBuzz():
    for i in range(1, 101):
        isThree = (i % 3 == 0)
        isFive = (i % 5 == 0)
        if (isThree):
            print("Fizz")
        elif (isFive):
            print("Buzz")
        elif (isThree) & (isFive):
            print("FizzBuzz")
        else:
            print(i)



def main():
    
    FizzBuzz()


main()
