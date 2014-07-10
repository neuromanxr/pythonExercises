

def main():
        
    boollist = []
    for i in range(100):
        boollist.append(False)

    for i in range(10):
        numbers = eval(input("Enter numbers: "))
        #boollist[i] = True
        isCovered(boollist, numbers)

    count = 0    
    for i in range(100):
        if boollist[i] == True:
            count += 1

    if count == 5:
        print("You win")
        print(boollist)
    else:
        print("You lose")
        print(boollist)
        
def isCovered(boollist, numbers):
    boollist[numbers - 1] = True



main()
