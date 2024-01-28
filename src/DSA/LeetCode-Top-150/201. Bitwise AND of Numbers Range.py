class Solution:

    # brute force - time limit exceeded
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        result = left
        for x in range(left+1, right + 1):
            result &= x
            
        return result
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        shiftCount = 0

        while left < right:
            left >>= 1
            right >>= 1
            shiftCount += 1

        result = left << shiftCount

        return result


    

s = Solution()
print(s.rangeBitwiseAnd(4, 7))
# print(s.rangeBitwiseAnd(10, 4))
# print(s.rangeBitwiseAnd(5, 7))
# print(s.rangeBitwiseAnd(1, 2147483647))
        