# https://leetcode.com/problems/valid-parentheses/


# Runtime: 33 ms, faster than 78.28% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 16.6 MB, less than 82.74% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:

        pMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        openP = set(['(','{','['])
        stack = []

        for x in s:
            if x in openP:
                stack.append(x)
                continue
            
            currOpenP = pMap[x]
            if not stack:
                return False
            
            currCloseP = stack.pop()
            if currOpenP != currCloseP:
                return False

        return True if not stack else False




    

s = Solution()
print(s.isValid(']'))
# print(s.isValid('()[]{}'))
# print(s.isValid('(]'))
# print(s.isValid('(('))
# print(s.isValid('('))