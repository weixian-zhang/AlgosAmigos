
from typing import List

class Solution:

    # brute force - time limit exceeded
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        count = 1

        def dfs(idx, tempCount):
            nonlocal count

            if idx + 1 > len(nums) - 1:
                return tempCount
            

            for x in range(idx + 1, len(nums)):
                if nums[idx] < nums[x]:
                    tempCount += 1
                    dfs(x, tempCount)
                    count = max(count, tempCount)
                    tempCount -= 1

            return tempCount


        for x in range(len(nums) - 2, -1, -1):
            tempCount = dfs(x, 1)
            count = max(count, tempCount)


        return count
    

    # dp bottom up tabular
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums) #[1 for x in range(len(nums))]

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    

s = Solution()
# print(s.lengthOfLIS([1,2,4,3]))
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))