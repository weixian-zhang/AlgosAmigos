class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []
        potentialCombo = []
        
        chosen = []
        
        candidates.sort()
        nums = list(candidates)
        
        def _backtrack(nums):

              
            #base case
            if sum(potentialCombo) > target:
                return
            
            if len(potentialCombo) > 0 and sum(potentialCombo) == target:
                
                result.append(potentialCombo.copy())
                return
            
            if nums == []:
                return
            
            prev = -1
            
            for i in range(len(nums)):
                
                if prev == nums[i]:
                    continue
                
                potentialCombo.append(nums[i])
                
                _backtrack(nums[i+1:])
                
                potentialCombo.pop()
                
                prev = nums[i]
                
        
        _backtrack(nums)
        
        return result #[x for x in result.values()]
    
    
if __name__ == '__main__':
    s = Solution()
    #r = s.combinationSum2([10,1,2,7,6,1,5], 8)
    r = s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27)
    print(r)
                
    