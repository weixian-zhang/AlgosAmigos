class Solution:
    def reverseVowels(self, s: str) -> str:
        
        if len(s) == 0 or len(s) == 1:
            return s
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        leftPointer = 0
        rightPointer = len(s) - 1
        
        strList = list(s)
        
        while leftPointer <= rightPointer:
            
            while leftPointer < len(strList) - 1:
                
                if strList[leftPointer].lower() in  vowels:
                    break
                else:
                    leftPointer += 1
                    
            while rightPointer > leftPointer:
                
                if strList[rightPointer].lower() in vowels:
                    break
                else:
                    rightPointer -= 1
            
            if (strList[leftPointer].lower() in  vowels) and strList[rightPointer].lower() in vowels:
                self.swap(strList, leftPointer, rightPointer)
            
            leftPointer += 1
            rightPointer -= 1
        
        return ''.join(strList)
            
    
    def swap(self, strList, srcIdx, destIdx):
        
        temp = strList[srcIdx]
        strList[srcIdx] = strList[destIdx]
        strList[destIdx] = temp
        
        
if __name__ == '__main__':
    s = Solution()
    
    print(s.reverseVowels('leetcode'))
        
        
        