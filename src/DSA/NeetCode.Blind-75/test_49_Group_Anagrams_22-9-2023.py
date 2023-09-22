class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        groupSorted = []
        result = []
        groupAnagrams = {}
        
        for x in strs:
            dicTemp = {}
            sortedVal = ''.join(sorted(x)) #sum([ord(s) for s in x])
            dicTemp[x] = sortedVal
            groupSorted.append(dicTemp)
            
        for dic in groupSorted:
            
            for k, v in dic.items():
            
                if v not in groupAnagrams:
                    
                    temp = []
                    temp.append(k)
                    groupAnagrams[v] = temp
                
                else:
                    
                    groupAnagrams[v].append(k)
                
        
        for k, v in groupAnagrams.items():
            
            result.append(v)
            
        return result
        
        

if __name__ == '__main__':
    s = Solution()
    
    r = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])#["cab","tin","pew","duh","may","ill","buy","bar","max","doc"])#["",""])#["eat","tea","tan","ate","nat","bat"])
    
    print(r)