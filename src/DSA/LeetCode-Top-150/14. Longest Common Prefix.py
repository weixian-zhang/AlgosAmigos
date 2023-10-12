class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        longestWord = 0
        
        for s in strs:
            longestWord = max(longestWord, len(s))
            
        i, j = 0, 0
        sameChar = set()
        result = []
        
        while i <= len(strs) - 1:
        
            word = strs[i]
            
            if j <= longestWord - 1:
                sameChar.add(word[j])
                    
            if i == len(strs) - 1:
                
                if len(sameChar) == 1:
                    result.append(list(sameChar)[0])
                    sameChar = set()
                    i = 0
                    j += 1
                else:
                    break
            else:      
                i += 1
                
        return ''.join(result)
                
                
    

if __name__ == '__main__':
    
    s = Solution()
    #print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["","b"]))