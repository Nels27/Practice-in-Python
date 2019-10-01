def strSwapper(toBeChanged): 
    a = len(toBeChanged)
    finalStr = ''
    c = a % 2
    tempFront = ''
    tempBack = ''
    tempCenter = ''
    oddMid = int((a-1)/2)
    evenMid = int(a/2)

    if c > 0:

        tempCenter = toBeChanged[int((a-1)/2)]
        finalStr = tempCenter

        for i in range(0,int((a-1)/2)):
            tempBack = toBeChanged[oddMid - (i+1)]
            tempFront = toBeChanged[oddMid + (i+1)]
            finalStr = tempFront + finalStr + tempBack

    else: 

        for i in range(0,int(a/2)):
            tempBack = toBeChanged[evenMid - (i+1)]
            tempFront = toBeChanged[evenMid + (i)]
            finalStr = tempFront + finalStr + tempBack
    
    return finalStr

def main():

    strManip = str(input('Enter string to be reversed:'))

    finalResult = strSwapper(strManip)

    print(strManip)
    print(finalResult)


if __name__ == "__main__":
    main()