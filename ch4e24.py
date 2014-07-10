import random

clubs, diamonds, hearts, spades = 15,16,17,18

ace, two, three, four, five, six, seven, eight, nine, \
     ten, jack, queen, king = 1,2,3,4,5,6,7,8,10,11,12,13,14

rankPick = random.randrange(1, 14)
suitPick = random.randrange(15, 19)


if rankPick == 1:
    rankPick = "Ace"
elif rankPick == 2:
    rankPick = "Two"
elif rankPick == 3:
    rankPick = "Three"
elif rankPick == 4:
    rankPick = "Four"
elif rankPick == 5:
    rankPick = "Five"
elif rankPick == 6:
    rankPick = "Six"
elif rankPick == 7:
    rankPick = "Seven"
elif rankPick == 8:
    rankPick = "Eight"
elif rankPick == 9:
    rankPick = "Nine"
elif rankPick == 10:
    rankPick = "Ten"
elif rankPick == 11:
    rankPick = "Jack"
elif rankPick == 12:
    rankPick = "Queen"
elif rankPick == 13:
    rankPick = "King"

if suitPick == 15:
    suitPick = "Clubs"
if suitPick == 16:
    suitPick = "Diamonds"
if suitPick == 17:
    suitPick = "Spades"
if suitPick == 18:
    suitPick = "Hearts"


print("Your card is ", rankPick, "of", suitPick)
