import random


lottery = random.randint(0, 99)
guess = eval(input("Enter two digits: "))

lotteryFirstDigit = (lottery // 10)
lotterySecondDigit = lottery % 10

guessFirstDigit = (guess // 10)
guessSecondDigit = guess % 10

#if (lotteryFirstDigit == guessFirstDigit) or \
#   (lotterySecondDigit == guessSecondDigit):
#    print("1000 added")
if guess == lottery:
    print(lottery, ",10000 added")    #match all
elif (guessFirstDigit == lotterySecondDigit) and \
   (guessSecondDigit == lotteryFirstDigit):
    print(lottery, ",5000 added")     #match digits
elif (guessFirstDigit == lotteryFirstDigit
    or guessFirstDigit == lotterySecondDigit
    or guessSecondDigit == lotteryFirstDigit
    or guessSecondDigit == lotterySecondDigit):
    print(lottery, ",1000 added")    #match one digit
else:
    print("No match")




#if (lottery % 10 == guess % 10) or \
#   (int(lottery / 10) == int(guess / 10)):
#    print("$1000 granted")
