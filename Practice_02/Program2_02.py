'''
    2. Accept one number from user and print that number of * on screen using While loop.

'''

def Display(Value):
    i = 1

    while(i <= Value):
        print("*", end = " ")
        i = i + 1

def main():
    print("Enter a Number : ")

    try:
        No = int(input())  # Accept input and convert to integer

        if(No < 0):
            print("Invalid Input..! Enter Numeric Values..!")
            return

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return

    Display(No)

if __name__ == "__main__":
    main()