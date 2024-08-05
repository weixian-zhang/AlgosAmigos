
from collections import deque
class Solution:

    # wrong answer
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        s1l = deque(list(s1))
        s2l = deque(list(s2))
        S3 = len(s3)
        i, j, h = 0, 0, 0

        inS1, inS2 = False, False

        while i <= S3 - 1:

            while len(s1l) > 0 and i <= S3 - 1 and s3[i] == s1l[0]:
                s1l.popleft()
                i += 1
                inS1 = True
            
            while len(s2l) > 0 and i <= S3 - 1 and s3[i] == s2l[0]:
                s2l.popleft()
                i += 1
                inS2 = True

            if not inS1 and not inS2:
                return False
            
            inS1, inS2 = False, False
        
        return len(s1l) == 0 and len(s2l) == 0
    

    # top down
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if s1 == '' and s2 == '' and s3 == '': return True
        
        if len(s1) + len(s2) != len(s3): return False

        S1L = len(s1) - 1
        S2L = len(s2) - 1

        dp = {}
        
        def dfs(i, j, result) -> bool:

            if (i,j) in dp:
                return dp[(i,j)]
            
            if i + j == len(s3):
                return True
            
            if s1 and i <= S1L and s1[i] == s3[i + j]:
                result = dfs(i + 1, j, result)

            if s2 and j <= S2L and s2[j] == s3[i + j]:
                result = dfs(i, j + 1, result)

            dp[(i, j)] = result

            return result

        
        return dfs(0, 0, False)




s = Solution()
print(s.isInterleave('a', '', 'a'))
print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
# print(s.isInterleave('', '', ''))
#print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
# print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
# print(s.isInterleave('a', 'b', 'a'))
print(s.isInterleave('aa', 'ab', 'aaba'))