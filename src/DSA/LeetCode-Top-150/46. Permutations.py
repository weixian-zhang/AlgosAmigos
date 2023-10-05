class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result = []
        lenOfNums = len(nums)
        
        def _backtrack(nums: list[int], tempArr: list[int]):
            
            # base case
            if len(tempArr) == lenOfNums:
                result.append(tempArr.copy())
                return
            
            for idx in range(len(nums)):
                
                tempArr.append(nums[idx])
                
                newNums = nums.copy()
                newNums.pop(idx)
                _backtrack(newNums, tempArr)
                
                tempArr.pop()
                
        
        _backtrack(nums, [])
        
        return result
    
    
    
    
if __name__ == '__main__':
    s = Solution()
    
    print(s.permute([1,2,3]))
        