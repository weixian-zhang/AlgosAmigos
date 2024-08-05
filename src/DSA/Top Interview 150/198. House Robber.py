from typing import List

class Solution:

    # brute force - Time Limit Exceeded
    def rob(self, nums: list[int]) -> int:
        
        cache = {}
        maxMoney = 0

        def dfs(i: int, currMoney):
            nonlocal maxMoney

            if i > len(nums) - 1:
                return
            
            if i in cache and cache[i] > maxMoney:
                return cache[i]

            currMoney += nums[i]
            
            maxMoney = max(maxMoney, currMoney)

            dfs(i + 2, currMoney)

            dfs(i + 3, currMoney)

            cache[i] = maxMoney
            
        dfs(0, 0)

        dfs(1, 0)
        
        return maxMoney

    def rob(self, nums: List[int]) -> int:
        
        self.memo = {}
        
        return self.robFrom(0, nums)
    
    def robFrom(self, i, nums):
        
        # No more houses left to examine.
        if i >= len(nums):
            return 0
        
        # Return cached value.
        if i in self.memo:
            return self.memo[i]

        one = self.robFrom(i + 1, nums)

        onePlus2 = self.robFrom(i + 2, nums) + nums[i]

        ans = max(one, onePlus2)
        
        # Recursive relation evaluation to get the optimal answer.
        # ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])
        
        # Cache for future use.
        self.memo[i] = ans
        return ans


s = Solution()
# print(s.rob([1,2,1,1]))
# print(s.rob([1,2]))
# print(s.rob([2,1,1,2]))
# print(s.rob([1,1]))
print(s.rob([1,2,3,1]))
# print(s.rob([2,7,9,3,1]))