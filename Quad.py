class Quad:
    def __init__(self, A, B, C):
        self.__A = A
        self.__B = B
        self.__C = C

    def getDiscriminant(self):
        discriminant = self.__B * self.__B - 4 * self.__A * self.__C
        return discriminant

    def getRoot1(self):
        root1 = (-self.__B + (self.__B * self.__B - 4 * self.__A * self.__C) * 0.5) / (2 * self.__A)
        return root1

    def getRoot2(self):
        root2 = (-self.__B - (self.__B * self.__B - 4 * self.__A * self.__C) * 0.5) / (2 * self.__A)
        return root2
