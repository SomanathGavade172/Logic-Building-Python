'''
    4. Accept one number and check whether is is divisible by 5 or not.

'''
def ChkDivisible(Value):
    if(Value % 5 == 0):
        return True
    else:
        return False

def main():
    print("Enter a Number : ")

    try:
        No = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return 
    
    Ret = ChkDivisible(No)

    if(Ret == True):
        print(No, "is Divisible by 5")
    else:
        print(No, "is Not Divisible by 5")

if __name__ == "__main__":
    main()