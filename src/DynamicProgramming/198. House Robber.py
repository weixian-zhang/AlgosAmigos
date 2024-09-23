class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        N = len(nums)
        dp = [0] * N

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for x in range(2, N):
            dp[x] = max(nums[x] + dp[x-2], dp[x - 1])

        return dp[-1]

s = Solution()
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))