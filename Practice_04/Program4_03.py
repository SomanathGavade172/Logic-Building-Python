'''
    3.Write a program which accept number from user and display all its non factors.

    Input  : 12
    Output : 5 7 8 9 10 11

    Input  : 13
    Output : 2 3 4 5 6 7 8 9 10 11 12

    Input  : 10
    Output : 3 4 6 7 8 9

'''

def NonFact(iValue):
   
    for i in range(1, iValue + 1 , 1):
        if(iValue % i != 0):
            print(i, end = " ") 
            
def main():

    print("Enter a Number : ")
    try:
        iNo = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    NonFact(iNo)

if __name__ == "__main__":
    main()