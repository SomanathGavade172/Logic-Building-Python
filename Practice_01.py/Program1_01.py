'''
    1. Program to divide two numbers

'''
def Divided(Value1, Value2):
    Result = 0
    Result = Value1 / Value2
    return Result    

def main():
    print("Enter First Numer : ")

    try:
        No1 = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return 
    
    print("Enter Second Numer : ")

    try:
        No2 = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return 

    Ret = Divided(No1, No2)

    print("Division is : ", Ret)

if __name__ == "__main__":
    main()