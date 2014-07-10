import random

score = random.randrange(70, 150)

pay = 5000
payRaise3 = 0.03
payRaise1 = 0.01

print("Your pay is ", pay)
print("Your score is ", score)

if score > 90:
    print("Your pay increased to ", format(payRaise3, ".2%"))
    print((payRaise3 + 1) * pay)
else:
    print("Your pay increased to ", format(payRaise1, ".2%"))
    print((payRaise1 + 1) * pay)
    
