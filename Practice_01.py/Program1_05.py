'''
    5. Accept one number from user and print that number of * on screen.

'''
def Accept(Value):
    for i in range(Value):
        print("*" , end = " ")

def main():
    print("Enter a Numebr : ")

    try:
        No = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    Accept(No)

if __name__ == "__main__":
    main()