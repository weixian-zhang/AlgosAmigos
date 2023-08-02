class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        unique = set(nums)
        
        if len(nums) != len(unique):
            return True
        
        return False