class Solution:
    
    def canJump(self, nums: list[int]) -> bool:
        
        cache = {}
        lastIndex = len(nums) - 1
        
        def _backtrack(jumpIndex: int) -> bool:
            
            if jumpIndex in cache:
                return cache[jumpIndex]
            
            if jumpIndex >= lastIndex:
                return  True
            
            if jumpIndex + nums[jumpIndex] >= lastIndex:
                return True
        
            
            for stepChoice in range(1, nums[jumpIndex] + 1):
                
                
                canReachLast = _backtrack(jumpIndex + stepChoice)
                    
                if canReachLast:
                    return True
                
                if jumpIndex not in cache:
                    cache[jumpIndex] = canReachLast
                    
                    
            return False
            
        return _backtrack(0)
        
    
    # def canJump(self, nums: list[int]) -> bool:
        
    #     i = 0
    #     stepsToJump = 0
    #     lastIndex = len(nums) - 1
        
    #     while i <= lastIndex:
            
    #         # determine steps tp jump
    #         if i == lastIndex:
    #             return True
    #         if nums[i] == 0:
    #             return False
    #         elif nums[i] - 1 == 0:
    #             stepsToJump = 1
    #         else:
    #             stepsToJump = nums[i] - 1
            
    #         # jump to step with checks of over bound
    #         if i + stepsToJump == lastIndex:
    #             return True
    #         elif i + stepsToJump > lastIndex:
    #             return False
    #         else:
    #             i += stepsToJump
        
    #     return False

    
s = Solution()
# print(s.canJump([2,0,0]))
# print(s.canJump([1]))
# print(s.canJump([0]))
#print(s.canJump([2,3,1,1,4]))
print(s.canJump([3,2,1,0,4]))