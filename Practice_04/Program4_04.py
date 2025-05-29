'''
    4.Write a program which accept number from user and return summation of all its non factors.

    Input  : 12
    Output : 50

    Input  : 10
    Output : 37

'''

def SumNonFact(iValue):
    iSum = 0
   
    for i in range(1, iValue + 1 , 1):
        if(iValue % i != 0):
            iSum = iSum + i

    return iSum
            
def main():

    print("Enter a Number : ")
    try:
        iNo = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    iRet = SumNonFact(iNo)

    print("Summation of Non Factors is : ", iRet)

if __name__ == "__main__":
    main()