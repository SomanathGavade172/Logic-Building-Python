'''
    2. Program to print 5 times “Marvellous” on screen.

'''

def Display(Value):
    for i in range(Value):
        print("Marvellous")

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