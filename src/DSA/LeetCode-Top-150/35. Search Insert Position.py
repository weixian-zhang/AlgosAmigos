class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return low
    
    
    
s = Solution()
# print(s.searchInsert([1,3], 0))
# print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
#print(s.searchInsert([1,3,5,6], 7))