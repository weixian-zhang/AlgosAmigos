class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
         
         wordMap = {}
         
         uniqueS = self.get_unique_chars(s)
         uniqueT = self.get_unique_chars(t)
         
         if len(uniqueS) != len(uniqueT):
             return False
         
         for x in range(len(uniqueS)):
             wordMap[uniqueS[x]] = uniqueT[x]
             
         generatedS = ''
         
         for x in s:
             generatedS += wordMap[x]
             
         return generatedS == t
        
    def get_unique_chars(self, s: str):
        uniqueChar = []
        for x in s:
            if x not in uniqueChar:
                uniqueChar.append(x)
        return uniqueChar
         
    
if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic('badc', 'baba'))
    # print(s.isIsomorphic('egg', 'add'))
    # print(s.isIsomorphic('foo', 'bar'))
    # print(s.isIsomorphic('paper', 'title'))