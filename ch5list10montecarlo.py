import random
import math

TRIALS = 1000000
numberOfHits = 0

for counter in range(TRIALS):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        numberOfHits += 1

pi = 4 * numberOfHits / TRIALS

print("pi is: ", pi)
                          
