'''
    2.Write a program which accept number from user and display its factors in decreasing order.

    Input  : 12
    Output : 6 4 3 2 1

    Input  : 13
    Output : 1

    Input  : 10
    Output : 5 2 1

'''


def FactRev(iValue):

    for i in range(iValue , 1):
        if(iValue % i == 0):
            print(i, end = " ")

        print()
            

def main():
    print("Enter a Number : ")

    try:
        iNo = int(input())

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..")
        return
    
    FactRev(iNo)

if __name__ == "__main__":
    main()