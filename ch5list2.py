import random

number = random.randrange(0, 100)

guess = -1
while guess != number:

    guess = eval(input("Guess number generated: "))

    if guess == number:
        print("right")
    elif guess > number:
        print("lower")
    else:
        print("highter")
    
        
