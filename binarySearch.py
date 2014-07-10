def main():
    lst = [2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79]

    number = eval(input("Enter search parameter: "))

    location = binary(number, lst)
    print(location)

##def binary(number, lst):
##    low = 0
##    high = len(lst) - 1
##    middle = (high + low) // 2
##    if number < lst[middle]:
##        high = middle - 1
##        for i in range(low, high):
##            if number == lst[i]:
##                print("Number is in: ", i)
##
##
##    if number > lst[middle]:
##        low = middle
##        high = len(lst)
##        for i in range(low, high):
##            if number == lst[i]:
##                print("Number is in: ", i)
        
def binary(number, lst):
    low = 0
    high = len(lst) - 1

    while high >= low:
        middle = (high + low) // 2
        if number < lst[middle]:
            high = middle - 1
        elif number == lst[middle]:
            return middle
        else:
            low = middle + 1
    return -low - 1



main()            
        
        
        
