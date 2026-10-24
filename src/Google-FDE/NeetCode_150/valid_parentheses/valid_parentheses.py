class Solution:
    def isValid(self, s: str) -> bool:

        # if len(s) % 2:
        #     return False
        
        open_parenthesis = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        stack = []

        for char in s:
            if char in open_parenthesis:
                stack.append(char)
            else:
                if not stack:
                    return False
                    
                open_p= stack.pop()
                close_p= open_parenthesis[open_p]

                if close_p != char:
                    return False


        return not stack


s = Solution()
print(s.isValid('('))
