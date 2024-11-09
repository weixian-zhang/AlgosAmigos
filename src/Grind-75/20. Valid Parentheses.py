class Solution:
    def isValid(self, s: str) -> bool:

        openp_map = {
            '(' : ')', 
            '{':'}',
            '[':']'
        }

        stack = []

        for i in range(len(s)):
            if s[i] in openp_map:
                stack.append(s[i])
                continue

            if stack:
                open_p = stack.pop(-1)
                close_p = openp_map[open_p]
                if close_p != s[i]:
                    return False
            else:
                return False

        return True if not stack else False


            
        