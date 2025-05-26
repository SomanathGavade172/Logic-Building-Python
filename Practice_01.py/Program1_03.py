'''
    3. Program to print 5 to 1 numbers on screen.

'''
def Display(Value):
    for i in range(Value, 0, -1):
        print(i)

def main():
    print("Enter a Number : ")

    try:
        No = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return
    
    Display(No)

if __name__ == "__main__":
    main()