'''
    5.Write a program which accept number from user and return difference between summation of all its factors and non factors.

    Input  : 12
    Output : -34 (16 - 50)

    Input  : 10
    Output : -29 (8 - 37)

'''

def SumNonFact(iValue):
    iSumNonFact = 0
    iSumFact = 0
   
    for i in range(1, iValue , 1):
        if(iValue % i == 0):
            iSumFact = iSumFact + i
        else:
            iSumNonFact = iSumNonFact + i

    return iSumFact - iSumNonFact
  
            
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