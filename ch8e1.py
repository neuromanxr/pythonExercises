class ssn:
    def __init__(self, ssnumber):
        self.__ssnumber = ssnumber

    def isSSN(self):
        test = False
        if len(self.__ssnumber) == 11:
            for i in range(len(self.__ssnumber)):
                ch = self.__ssnumber[i]
                if '0' <= ch <= '9' and self.__ssnumber[3] == '-' and self.__ssnumber[6] == '-':
                    test = True
                else:
                    test = False
        if test == True:
            print("Is SSN")
        else:
            print("Not SSN")




def main():
    ssnumber1 = input("Enter SSN: ")
    ssn1 = ssn(ssnumber1)
    ssn1.isSSN()
    
    ##isSSN(ssnumber)

##def isSSN(ssnumber):
##    test = False
##    if len(ssnumber) == 11:
##        for i in range(len(ssnumber)):
##            ch = ssnumber[i]
##            if '0' <= ch <= '9' and ssnumber[3] == '-' and ssnumber[6] == '-':
##                test = True
##            else:
##                test = False
##    if test == True:
##        print("Is SSN")
##    else:
##        print("Not SSN")





main()
