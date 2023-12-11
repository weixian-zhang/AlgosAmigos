class Solution:

    # top-down, recursion + memoization
    def rob(self, nums: list[int]) -> int:
        
        maxRob = 0
        dpCache = {}
        def recurse(idx: int):

            if idx > len(nums) - 1:
                return 0
            
            if idx in dpCache:
                return dpCache[idx]
            
            dpCache[idx] = max(nums[idx] + recurse(idx + 2), recurse(idx + 1))
            return dpCache[idx]

        recurse(0)
        
        return maxRob
    

    def rob(self, nums: list[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0 for x in range(len(nums))]

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for x in range(2, len(nums), 1):
            dp[x] = max(nums[x] + dp[x - 2], dp[x - 1])

        return dp[-1]


    # my solution - exceed time complexity
    # def rob(self, nums: list[int]) -> int:
        
    #     if not nums:
    #         return 0
    #     if len(nums) == 1:
    #         return nums[0]
        
    #     maxRob = 0
    #     tempRob = 0
    #     dpCache = {}

    #     def recurse(idx: int):
    #         nonlocal maxRob
    #         nonlocal tempRob

    #         if idx < 0:
    #             return tempRob
            
    #         tempRob += nums[idx]

    #         if idx in dpCache :
    #             return dpCache[idx]

    #         recurse(idx - 2)

    #         #recurse(idx - 3)

    #         maxRob = max(tempRob, maxRob)
            
    #         dpCache[idx] = tempRob
                    
    #         tempRob -= nums[idx]
        
    #     for x in range(len(nums)-1, -1, -1):
    #         recurse(x)
    #         tempRob = 0

    #     return maxRob

s = Solution()
# print(s.rob([6,6,4,8,4,3,3,10]))
#print(s.rob([1,2,1,1]))
# print(s.rob([4,1,2,7,5,3,1]))
print(s.rob([2,1,1,2]))  # 4
# print(s.rob([1,1]))
# print(s.rob([]))
# print(s.rob([10]))    #10
# print(s.rob([1,2,3,1]))    #4
# print(s.rob([2,7,9,3,1]))  #12