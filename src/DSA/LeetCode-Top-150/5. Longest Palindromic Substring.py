class Solution:

    # 2 pointers - wrong answer
    def longestPalindrome(self, s: str) -> str:
        
        N = len(s)
        left, right = 0, 0
        longestSoFar = ''

        mid = len(s) // 2
        if len(s) % 2 == 0:
            left, right = mid - 1, mid
        else:
            left, right = mid, mid

        longestSoFar = s[left]

        while left >= 0 and right <= N - 1:


            if s[left] == s[right]:
                longestSoFar = s[left:right + 1] if len(s[left:right + 1]) > len(longestSoFar) else longestSoFar

            if s[left] == s[right + 1 if right + 1 <= N-1 else right]:
                longestSoFar = s[left:right + 2] if len(s[left:right + 2]) > len(longestSoFar) else longestSoFar

            if s[left-1 if left - 1 >= 0 else left] == s[right]:
                longestSoFar = s[left - 1: right + 1] if len(s[left - 1: right + 1]) > len(longestSoFar) else longestSoFar


            left -= 1
            right += 1

        return longestSoFar
    

    # top down - recursion - time lmit exceeded
    def longestPalindrome(self, s: str) -> str:
        
        N = len(s)
        longestSoFar = ''

        def isPalindrome(subStr):
            
            mid = len(subStr) // 2
            left, right = mid, mid
            if len(subStr) % 2 == 0:
                left, right = mid - 1, mid

            while left >= 0 and right <= len(subStr) - 1:
                if subStr[left] != subStr[right]:
                    return False
                left -= 1
                right += 1
            
            return True


        def dfs(i, j, localPalindrome):

            currSubStr = s[i:j + 1]

            # base case
            if j > N - 1 or i > N - 1:
                return localPalindrome
            
            if  isPalindrome(currSubStr): # currSubStr == currSubStr[::-1]: #
                localPalindrome = currSubStr if len(currSubStr) > len(localPalindrome) else localPalindrome

            return dfs(i, j + 1, localPalindrome)

            
        for x in range(len(s)):
            localPalindrome = dfs(x, x, '')
            longestSoFar = localPalindrome if len(localPalindrome) > len(longestSoFar) else longestSoFar

        return longestSoFar


    # foreach char, make it a "middle" char of palindrome
    def longestPalindrome(self, s: str) -> str:

        
        N = len(s)
        result = ''
        resultLen = 0

        for i in range(len(s)):

            # odd length word
            left, right = i, i

            while left >= 0 and right <= N - 1 and s[left] == s[right]:
                if (right - left) + 1 > len(result):
                    result = s[left: right + 1]
                
                left -= 1
                right += 1

            # even length word
            left, right = i, i + 1
            while left >= 0 and right <= N - 1 and s[left] == s[right]:
                if (right - left) + 1 > len(result):
                    result = s[left: right + 1]
                
                left -= 1
                right += 1

        
        return result


            

        


    


s = Solution()

print(s.longestPalindrome('eabcb')) # bcb
print(s.longestPalindrome('aab')) # aa
print(s.longestPalindrome('ac')) # a
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('malayalam'))



