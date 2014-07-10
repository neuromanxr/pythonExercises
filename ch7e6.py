from Quad import Quad

def main():

    intA = eval(input("Enter integer: "))
    intB = eval(input("Enter integer: "))
    intC = eval(input("Enter integer: "))
    
    quad1 = Quad(intA, intB, intC)

    print("Discriminant is: ", quad1.getDiscriminant())
    print("Root 1 is: ", quad1.getRoot1())
    print("Root 2 is: ", quad1.getRoot2())


main()
