
import pdb

def swapFunc(firstInd, secInd, dataList):
    a = dataList[firstInd]
    b = dataList[secInd]
    dataList[firstInd] = b
    dataList[secInd] = a


def zeroFinder(data):
    i = 0
    k = 1
    while (i < len(data) - 1):
        pdb.set_trace()
        if(data[i] == 0):
            if(data[len(data) - (k)] != 0):
                swapFunc(i,len(data) - k,data)
            else:
                k = k+1
        else:
            i = i+1



        #if(data[i] == 0):
         #   for k in range(i+1,len(data)):
          #      if(data[len(data) - k] != 0):
           #         swapFunc(i,len(data) - k,data)



def main():
    data = [0,2,3,0]
    zeroFinder(data)
    #pdb.set_trace()
    print(data)



if __name__ == "__main__":
    main()
