'''
    2. Write a program which accept number from user and print even factors of that number.

    Input  : 24
    Output : 2 4 6 8 12
'''

def DisplayFactor(iValue):
    for i in range(1, iValue + 1):
        if(iValue % i == 0 and i % 2 == 0):
            print(i, end = " ")

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

    DisplayFactor(iNo)


if __name__ == "__main__":
    main()