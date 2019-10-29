#String Reflect across an axis



def strReflect(str2BeChanged):
    tempFrnt = ''
    tempBack = ''
    strLength = len(str2BeChanged)
    rem = strLength % 2
    oddMid = int((strLength - 1)/ 2)
    evenMid = int(strLength/2)

    finalStr = ''

    if (rem > 0):
        finalStr = str2BeChanged[oddMid]
        for i in range(0,oddMid):
            tempFrnt = str2BeChanged[strLength - (i+1)]
            tempBack = str2BeChanged[i]
            finalStr = tempFrnt + finalStr + tempBack
    elif (strLength == 1):
        print("This is a char and can't be reversed")

    else:
        for i in range(0,evenMid):
            tempFrnt = str2BeChanged[strLength - (i+1)]
            tempBack = str2BeChanged[i]
            finalStr = tempFrnt + finalStr + tempBack

    return(finalStr)


def main():
    strManip = input('Input the string you want reversed \n')
    
    strChanged = strReflect(strManip)

    print('Changed string: {}'.format(strChanged))
    #print(strChanged)





if __name__ == "__main__":
    main()