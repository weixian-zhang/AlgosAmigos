from typing import List

class Solution:

    # kadane's algorithm does not work
    def maxProduct(self, nums: List[int]) -> int:

        maxSoFar, max_total = 1, min(nums)#max(nums + [0])

        for x in range(len(nums)):
            maxSoFar = max(nums[x] * maxSoFar,  nums[x])
            max_total = max(max_total,maxSoFar )

        return max_total
    
    # prefix algorithm - does not work
    # 2 prefix sum - left prefix and right prefix
    # get max from 2 prefix 
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        maxSoFar = max(nums)
        left_prefix, right_prefix = 1, 1
        
        for i in range( n):
            j = -1 - i # right to left index

            left_prefix = 1 if left_prefix == 0 else left_prefix
            right_prefix = 1 if right_prefix== 0 else right_prefix

            left_prefix *= nums[i]

            right_prefix *= nums[j]

        
            maxSoFar = max(maxSoFar, left_prefix, right_prefix)

        return maxSoFar


            


s = Solution()


print(s.maxProduct([-1,-2,-3,0]))
# print(s.maxProduct([-3,0,1,-2])) # 1
# print(s.maxProduct([-2,3,-4])) # 24
# print(s.maxProduct([-2,0,-1])) # 0
# print(s.maxProduct([2,3,-2,4])) # 6