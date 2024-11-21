class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        new_s = []

        for i in range(len(s)):
            if not s[i].isalnum():
                continue 

            new_s.append(s[i])

        rs = ''.join(new_s[::-1])

        return True if ''.join(new_s) == rs else False
        