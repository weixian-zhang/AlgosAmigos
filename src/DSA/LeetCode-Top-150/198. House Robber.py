class Solution:
    def rob(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        maxRob = 0
        tempRob = 0
        dpCache = {}

        def recurse(idx: int):
            nonlocal maxRob
            nonlocal tempRob

            if idx > len(nums) - 1:
                return tempRob
            
            tempRob += nums[idx]

            # if idx in dpCache and tempRob <= dpCache[idx]:
            #     return dpCache[idx]

            recurse(idx + 2)

            recurse(idx + 3)

            maxRob = max(tempRob, maxRob)
            
            #dpCache[idx] = tempRob
                    
            tempRob -= nums[idx]
        
        for x in range(len(nums)):
            recurse(x)
            tempRob = 0

        return maxRob

s = Solution()
print(s.rob([6,6,4,8,4,3,3,10]))
#print(s.rob([1,2,1,1]))
# print(s.rob([4,1,2,7,5,3,1]))
# print(s.rob([2,1,1,2]))  #12
# print(s.rob([1,1]))
# print(s.rob([]))
# print(s.rob([10]))    #10
# print(s.rob([1,2,3,1]))    #4
# print(s.rob([2,7,9,3,1]))  #12