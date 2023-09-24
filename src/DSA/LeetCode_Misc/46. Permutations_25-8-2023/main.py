class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result = []
        
        result.extend([3,4])
        
        if len(nums) == 1:
            return [nums.copy()]
        
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            
            result.extend(perms)
            nums.append(n)
            
        return result
    
    
if __name__ == '__main__':
    s = Solution()
    
    s.permute([1,2,3])
        