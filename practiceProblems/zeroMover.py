
import pdb

def swapFunc(firstInd, secInd, dataList):
    a = dataList[firstInd]
    b = dataList[secInd]
    dataList[firstInd] = b
    dataList[secInd] = a



def zeroFinder(data):
    for i in range(0,len(data)):
        #pdb.set_trace()
        if(data[i] == 0):
            for k in range(i+1,len(data)):
                if(data[len(data)-k] != 0):
                    swapFunc(i,(len(data)-k),data)
                    break
                break



def main():
    data = [0,1,2,3,6,0,2]
    zeroFinder(data)
    #pdb.set_trace()
    print(data)



if __name__ == "__main__":
    main()
