'''
    1. Write a program which accept one number from user and print that number of even numbers on screen.

    Input  : 7
    Output : 2 4 6 8 10 12 14

'''
def PrintEven(iValue):
    for i in range(1, iValue + 1):
        print(i * 2 , end = " ")

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

    PrintEven(iNo)


if __name__ == "__main__":
    main()