class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        result = []
        
        nums = [x for x in range(1, n+1)]
        
        def _backtrack(nums, tempArr: list[int]):
            
            #base case
            if len(tempArr) == k:
                result.append(tempArr.copy())
                return

            for idx, x in enumerate(nums):
                
                tempArr.append(x)
                
                _backtrack(nums[idx+1:], tempArr)
                
                # backtracked
                tempArr.pop()
                
                
            
        _backtrack(nums, [])
        
        return result
    
    
    
if __name__ == '__main__':
    s = Solution()
    s.combine(4, 2)