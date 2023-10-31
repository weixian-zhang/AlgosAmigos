class Solution:
    
    # my solution dynamic programming
    def jump(self, nums: list[int]) -> int:
        
        lastIndex = len(nums) - 1
        minJump = 10000000
        dp = {}
        
        def _recurse(jumpIndex) -> int:
            nonlocal minJump
             
            if jumpIndex >= lastIndex:
                return 0
            
            if jumpIndex in dp:
                return dp[jumpIndex]
            
            for x in range(1, nums[jumpIndex] + 1):
                
                minJump = min(minJump, 1 + _recurse(jumpIndex + x))
                
                pass # this line will execute after "last func"/base case return
                
                dp[jumpIndex] = minJump
            
            return minJump
        
            
        jumps = _recurse(0)
        
        return jumps
        
    
    # solution attempt 1, doesn't work
    # def jump(self, nums: list[int]) -> int:
        
    #     lastIdx = len(nums) - 1
    #     result = 0
        
    #     def _recurse(currIndex: int):
            
    #         if currIndex >= lastIdx:
    #             return 0
            
    #         currIndex = self._get_max_steps(nums, currIndex)

    #         # each recursion is a move, which is the result
    #         return 1 + _recurse(currIndex)

    #     return _recurse(0)
    
    
    # def _get_max_steps(self, nums: list[int], currIdx: int):
        
    #     idxOfLargest = 0
    #     largest = 0
    #     for x in range(1, nums[currIdx] + 1):
    #         tempCurr = currIdx + x
            
    #         if tempCurr >= len(nums) - 1:
    #             return len(nums) - 1
            
    #         if nums[currIdx] + nums[tempCurr] > largest:
    #             largest = nums[currIdx] + nums[tempCurr]
    #             idxOfLargest = tempCurr
        
    #     return (idxOfLargest - currIdx) + currIdx
        
    
    
s = Solution()
# print(s.jump([2,3,1,1,4]))
# print(s.jump([2,3,0,1,4]))
# print(s.jump([2,0]))
# print(s.jump([1,1,1,1]))
# print(s.jump([3,2,1]))
# print(s.jump([2,1]))
# print(s.jump([1,2,1,1,1]))
print(s.jump([4,1,1,3,1,1,1]))