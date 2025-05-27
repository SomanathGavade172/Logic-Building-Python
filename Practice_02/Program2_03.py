'''
    3. Accept on number from user if number is less than 10 then print “Hello” otherwise print “Demo”.

'''
def Display(Value):
    if(Value < 10):
        print("Hello")
    else:
        print("Demo")

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