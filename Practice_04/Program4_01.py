'''
    1. Write a program which accept number from user and display its multiplication of factors.

    Input  : 12
    Output : 144 (1 * 2 * 3 * 4 * 6)

    Input  : 13
    Output : 1 (1)

    Input  : 10
    Output : 10 (1 * 2 * 5)

'''

def MultiFact(iValue):
    iMulti = 1

    for i in range(1, iValue):
        if(iValue % i == 0):
            iMulti = iMulti * i
    
    return iMulti

def main():
    print("Enter a Number : ")

    try:
        iNo = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..")
        return
    
    iRet = MultiFact(iNo)

    print("Multiplication of Factor is : ", iRet)

if __name__ == "__main__":
    main()