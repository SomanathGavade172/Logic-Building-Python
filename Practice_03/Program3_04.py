'''
    4. Accept one character from user and convert case of that character.

    Input  : a 
    Output : A
    
    Input  : D 
    Output : d

'''

def DisplayConvert(Char):
    if(Char >= 'A' and Char <= 'Z'):
        Char = chr(ord(Char) + 32)
        print(Char)
        
    elif(Char >= 'a' and Char <= 'z'):
        Char = chr(ord(Char) - 32)
        print(Char)

def main():
    print("Enter Character : ")

    try:
        cChar = str(input())

        if(len(cChar) != 1):
            print("Please Enter only One Character..!")
            return

    except(ValueError):
        print("Invalid Input..! Enter Numeric Values..!")
        return

    DisplayConvert(cChar)


if __name__ == "__main__":
    main()