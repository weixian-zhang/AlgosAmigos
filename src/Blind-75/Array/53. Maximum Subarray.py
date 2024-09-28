from typing  import List

class Solution:

    # brute force
    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        overall_max = -float('inf')

        i = 0
        
        while i <= n-1:
            
            local_sum = nums[i]
            sum_range = 0

            while i + sum_range <= n-1:
                local_sum = 0

                for y in range(i, i + sum_range + 1):
                    local_sum += nums[y]
                overall_max = max(local_sum, overall_max)
                sum_range += 1

            i += 1

        return overall_max

    # kadane's
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        maxSoFar, totalMax = 0, -float('inf')

        for i in range(n):

            maxSoFar = max(maxSoFar + nums[i], nums[i])

            totalMax = max(maxSoFar, totalMax)

        return totalMax


s = Solution()
print(s.maxSubArray([1]))
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))