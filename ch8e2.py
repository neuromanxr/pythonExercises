class substring:
    def __init__(self, sub1, string1):
        self.__sub1 = sub1
        self.__string1 = string1

    def findsub(self):
        if len(self.__string1) > len(self.__sub1):
            j = 0
            k = 0
            for i in range(len(self.__string1)):
                if self.__sub1[j] == self.__string1[i]:
                    k = i + 1
                    j += 1
                    if j == len(self.__sub1) - 1:
                        print(k - j)
                        break
                    #print(k)
                    
        else:
            print('-1')



def main():
    string1 = input("Enter string: ")
    sub1 = input("Enter sub: ")

    substring1 = substring(sub1, string1)
    substring1.findsub()


main()
