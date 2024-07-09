
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


s = Solution()
# print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
# print(s.isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
# print(s.isInterleave('a', 'b', 'a'))
print(s.isInterleave('aa', 'ab', 'aaba'))