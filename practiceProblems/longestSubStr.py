import pdb

def lengthOfLongestSubstring(var):
        """
        :type s: str
        :rtype: int
        """
        strLength = len(var)
        i = 0
        tempSub = ''
        subStrLen = 0
        strCnt = []
        


        for i in range(0,strLength):
            
            pdb.set_trace()
            if (var[i] in tempSub):
                #pdb.set_trace()
                tempSub = var[i]
                strCnt.append(subStrLen)
                subStrLen = 1  

            else:
                #pdb.set_trace()
                tempSub = tempSub + var[i]
                subStrLen += 1

        #pdb.set_trace()  
        # 
        if (strCnt != []):
            return(max(strCnt))

        else:
            return 0


def main():
    s = ''
    print(lengthOfLongestSubstring(s))
    

if __name__ == "__main__":
    main()