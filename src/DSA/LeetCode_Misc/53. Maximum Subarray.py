class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        curr_sum = nums[0]
        max_sum= curr_sum
        
        for x in range(1, len(nums)):
            
            curr_sum = max(nums[x], nums[x] + curr_sum)
            max_sum = max(max_sum, curr_sum)
        
        return max_sum