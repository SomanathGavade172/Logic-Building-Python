'''
    5. Accept number from user and check whether number is even or odd.

'''
def ChkEven(iValue):
    if(iValue % 2 == 0):
        return True
    else:
        return False

def main():
    print("Enter a Number : ")

    try:
        iNo = int(input())  # Accept input and convert to integer

        if(iNo < 0):
            print("Invalid Input..! Enter Numeric Values..!")
            return

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return

    iRet = ChkEven(iNo)

    if(iRet == True):
        print(iNo ,"is Even")
    else:
        print(iNo, "is Odd Number.")

if __name__ == "__main__":
    main()
