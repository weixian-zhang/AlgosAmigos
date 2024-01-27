
# string manipulation, not standard bitwise
class Solution:
    def hammingWeight(self, n: int) -> int:

        return len([x for x in str('{0:b}'.format(n)) if x == '1'])
        

# using bitwise operation
# Runtime: 45 ms, faster than 17.41% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 16.5 MB, less than 25.06% of Python3 online submissions for Number of 1 Bits.
class Solution:
    def hammingWeight(self, n: int) -> int:

        count = 0

        while n:

            if n & 1:
                count += 1 
            
            n >>= 1

        return count


s = Solution()
print(s.hammingWeight(50))
        