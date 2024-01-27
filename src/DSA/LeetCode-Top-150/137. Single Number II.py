
from typing import List

# my solution with sorting
# Runtime: 57 ms, faster than 77.09% of Python3 online submissions for Single Number II.
# Memory Usage: 18.7 MB, less than 62.23% of Python3 online submissions for Single Number II.
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        
        N = len(nums)

        if N == 1:
            return nums[0]
        
        nums.sort()

        i = 0
        while i <= N -1:
            
            for j in range(i, i + 2):
                
                if j + 1 <= N-1 and nums[j] != nums[j + 1]:
                    return nums[j]
            
            i += 3

        return nums[-1]


s = Solution()
print(s.singleNumber([0,1,0,1,0,1,99]))
# print(s.singleNumber([1,3,1,3,1,3,2]))