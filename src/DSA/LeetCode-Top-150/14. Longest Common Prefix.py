class Solution:
    
    # horizontal scan
    # time: O(n)
    # space: O(1)
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        
        if len(strs) == 0:
            return ''
        
         
        prefix = strs[0]
        prefixLen = len(prefix)
        
        for x in range(1, len(strs)):
            
            word = strs[x]
            
            # slice word or prefix to make them same length
            if len(word) > len(prefix):
                word = ''.join(word[:len(prefix)])
            else:
                prefix = ''.join(prefix[:len(word)])
            
            # checks if word starts with prefix, if not, truncate last-char of prefix and check again
            while len(prefix) >= 0:
                
                if word.startswith(prefix):
                    break
                else:
                    prefix = prefix[:-1]
                    
                    
        return prefix
    
    # my solution
    # time complexity: O(n), for each word in strs, compare each char "vertically"
    # f| l| o| wer
    # f| l| o| w
    # f| l| i| ght
    # space complexity: O(n + n), result and set 
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        import sys
        shortestWord = sys.maxsize
        
        for s in strs:
            shortestWord = min(shortestWord, len(s))
            
        i, j = 0, 0
        sameChar = set()
        result = []
        
        while i <= len(strs) - 1:
        
            word = strs[i]
            
            if j <= shortestWord - 1:
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
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    #print(s.longestCommonPrefix(["","b"]))