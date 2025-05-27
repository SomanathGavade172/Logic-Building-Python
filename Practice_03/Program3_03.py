'''
    3. Write a program which accept number from user and print even factors of that number.

    Input   : 36
    Output  : 2 4 6 12 18

'''
def DisplayEvenFactor(iValue):
    for i in range(2, iValue, 2):
        if(iValue % i == 0):
            print(i , end = " ")

def main():
    print("Enter a Number : ")

    try:
        iNo = int(input())

        if(iNo < 0):
            print("Please Enter +Ve Number..!")
            return
        
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return

    DisplayEvenFactor(iNo)


if __name__ == "__main__":
    main()