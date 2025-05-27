'''
    4. Accept two numbers from user and display first number in second number of times.

    Input  : 12 5
    Output : 12 12 12 12 12

    Input  : -2 3
    Output : -2 -2 -2

    Input  : 21 -3
    Output : 21 21 21

    Input  : -2 0
    Output :

'''
def Dispaly(iNo, iFrequency):
    for i in range(1, iFrequency + 1):
        print(iNo , end = " ")


def main():
    print("Enter a Number : ")
    iValue = int(input())

    print("Enter Frequency : ")
    iCount = int(input())
    
    Dispaly(iValue, iCount)


if __name__ == "__main__":
    main()