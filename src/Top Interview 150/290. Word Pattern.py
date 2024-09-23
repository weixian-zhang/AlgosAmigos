class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        patternMap = {}
        patternGeneratedString = []
        uniquePatterns = self.get_unique_items(pattern,'')#list(set(pattern))
        uniqueS = self.get_unique_items(s, ' ') #list(set(s.split(' ')))
        
        for p in range(len(uniquePatterns)):
            if p <= len(uniqueS) - 1:
                patternMap[uniquePatterns[p]] = uniqueS[p]
        
        for x in pattern:
            if x in patternMap:
                patternGeneratedString.append(patternMap[x])
            else:
                patternGeneratedString.append('')
            
        return ' '.join(patternGeneratedString) == s
    
    def get_unique_items(self, s: str, delimiter: str):
        
        uniqueItems = []
        if delimiter == '':
            splitted = s
        else:
            splitted = s.split(delimiter)
        
        for x in splitted:
            if x not in uniqueItems:
                uniqueItems.append(x)
        return uniqueItems
    
    
if __name__ == '__main__':
    
    s = Solution()
    print(s.wordPattern('deadbeef', "d e a d b e e f"))
    # print(s.wordPattern('abba', "dog dog dog dog"))
    # print(s.wordPattern('abba', "dog cat cat dog"))
    # print(s.wordPattern('abba', "dog cat cat fish"))
    # print(s.wordPattern('aaaa', "dog cat cat dog"))