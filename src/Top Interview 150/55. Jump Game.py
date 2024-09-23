class Solution:
    
    # greedy algorithm - start from last index/destination move backwards see if previous steps allow to move ahead
    # O(n)
    def canJump(self, nums: list[int]) -> bool:
        
        goal= len(nums) - 1   # start from second last item
        
        for x in range(goal, -1, -1):
            if x + nums[x] >= goal:
                goal = x
                
        return True if goal == 0 else False

    
    # Dynamic programming - recursion with memoization
    # O(n2)
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

    
s = Solution()
print(s.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
# print(s.canJump([2,0,0]))
# print(s.canJump([1]))
# print(s.canJump([0]))
#print(s.canJump([2,3,1,1,4]))
#print(s.canJump([3,2,1,0,4]))