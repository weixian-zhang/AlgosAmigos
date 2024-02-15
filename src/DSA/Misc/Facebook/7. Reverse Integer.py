# https://www.geeksforgeeks.org/reverse-digits-integer-overflow-handled/
# https://leetcode.com/problems/reverse-integer/

# Runtime: 39 ms, faster than 47.63% of Python3 online submissions for Reverse Integer.
# Memory Usage: 16.6 MB, less than 78.31% of Python3 online submissions for Reverse Integer.
class Solution:
    def reverse(self, x: int) -> int:
        
        
        isNeg = False
        revNum = 0

        if x < 0:
            isNeg = True
            # convert to positive anyway, handle negative when returning result
            x = -x
        
        numToRev = x

        min32Int = -2 ** 31
        max32Int =  2 ** 31

        while numToRev != 0:
            # join the number by multiply by 10 to get extra place on right

            modNum = numToRev % 10

            revNum = revNum * 10 + modNum
            
            numToRev = numToRev // 10

            if revNum <= min32Int or revNum >= max32Int:
                return 0

        return -revNum if isNeg else revNum


s = Solution()
print(s.reverse(1000000045))
print(s.reverse(-5896))