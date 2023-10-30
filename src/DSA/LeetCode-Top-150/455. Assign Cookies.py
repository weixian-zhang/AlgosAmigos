class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        
        g.sort()
        s.sort()
        
        result = 0
        for x in range(len(s)):
            
            j = 0
            while j <= len(g)-1:
                if g[j] <= s[x]:
                    result += 1
                    g.pop(j)
                    break
                else:
                    j += 1
                
        return result
    
    
s = Solution()
print(s.findContentChildren([1,2,3], [1,1]))
print(s.findContentChildren([1,2,3], [1,2]))
print(s.findContentChildren([10,9,8,7], [10,9,8,7]))
