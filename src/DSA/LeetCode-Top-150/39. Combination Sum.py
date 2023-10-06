class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []
        
        def _backtrack(nums: list[int], idx: int, tempResult: list[int]):
            
            
            # base cases
            if sum(tempResult) > target:
                return
            
            if sum(tempResult) == target:
                result.append(tempResult.copy())  
                return
            
            
            while idx <= len(nums)-1:
                
                tempResult.append(nums[idx])
                
                _backtrack(nums, idx, tempResult)
                
                # after backtracing
                tempResult.pop()
                
                idx += 1
        
        
        _backtrack(candidates, 0, [])
        
        return result
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))