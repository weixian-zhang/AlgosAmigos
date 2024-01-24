from typing import List

class Solution:

    # my solution, brute force - time limit exceeded
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        totalMax = nums[0]

        for start in range(len(nums)):
            maxSum = nums[start]
            currSum = maxSum

            for x in range(start + 1, len(nums) + start):

                x = x % len(nums)
                
                currSum = max(nums[x], nums[x] + currSum)
                maxSum = max(maxSum, currSum)
                totalMax = max(maxSum, totalMax)
         
        
        return totalMax
    
    # neetcode solution
    # keep track of both min and maxsum subarray and total minus min
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # keep track of both max and min sum of subarray
        globalMin, globalMax = nums[0], nums[0]
        currMin, currMax = 0, 0
        total = 0

        for x in nums:
            total += x

            currMax = max(x, x + currMax)
            globalMax = max(globalMax,currMax )

            currMin = min(x, x + currMin)
            globalMin = min(globalMin, currMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
    

s = Solution()
print(s.maxSubarraySumCircular([-5, 3, 5]))
# print(s.maxSubarraySumCircular([1,-2,3,-2]))
# print(s.maxSubarraySumCircular([5,-3,5]))