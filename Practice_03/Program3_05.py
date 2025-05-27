'''
    5. Accept on character from user and check whether that character is vowel(a,e,i,o,u) or not.

    Input  : E 
    Output : TRUE

    Input  : d 
    Output : FALSE

'''

def ChkVowel(cValue):
    if(cValue == 'a' or cValue == 'e' or cValue == 'i' or cValue == 'o' or cValue == 'u' or cValue == 'A' or cValue == 'E' or cValue == 'I' or cValue == 'O' or cValue == 'U'):
        return True
    else:
        return False

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

    bRet = ChkVowel(cChar)

    if(bRet == True):
        print("TRUE")
    else:
        print("FALSE")


if __name__ == "__main__":
    main()