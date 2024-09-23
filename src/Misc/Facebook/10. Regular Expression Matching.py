# https://leetcode.com/problems/regular-expression-matching/


# Runtime: 8857 ms, faster than 6.97% of Python3 online submissions for Regular Expression Matching.
# Memory Usage: 16.6 MB, less than 88.33% of Python3 online submissions for Regular Expression Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        S = len(s)
        P = len(p)
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            # s matches all of p and both went out of bounds
            if i >= S and j >= P:
                return True
            if j >= len(p):
                return False
            
            match = i < S and (p[j] == '.' or s[i] == p[j])

            if j + 1 < P and p[j + 1] == '*':
                cache[(i, j)] = (dfs(i, j + 2) or # dont use *
                        match and dfs(i + 1, j)) # use *
                return cache[(i, j)] 
    
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            
            return False
        
        return dfs(0,0)



    

s = Solution()
print(s.isMatch('aab', 'a*b*c'))