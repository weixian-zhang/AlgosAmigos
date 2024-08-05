from typing import List

# binary search
# my solution
# Runtime: 48 ms, faster than 65.86% of Python3 online submissions for Find Peak Element.
# Memory Usage: 16.6 MB, less than 70.58% of Python3 online submissions for Find Peak Element.

# neetcode solution
# Runtime: 47 ms, faster than 71.05% of Python3 online submissions for Find Peak Element.
# Memory Usage: 16.6 MB, less than 62.44% of Python3 online submissions for Find Peak Element.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binary_search(low: int, high: int):
            
            while low <= high:
                
                mid = low + ((high - low) // 2)
                
                # my solution
                # left = mid -1 if mid -1 >= 0 else mid
                # right = mid + 1 if mid + 1 <= len(nums) - 1 else mid
            
                # if nums[mid] >= nums[right] and nums[mid] >= nums[left]:
                #     return mid
                
                # # is right neighbour greater
                # elif nums[right] > nums[mid]:
                #     low = mid + 1

                # # is left neighbour greater
                # elif nums[left] > nums[mid]:
                #     high = mid - 1

                # neetcode code
                
                # is left neighbour greater
                if mid > 0 and nums[mid - 1] > nums[mid]:
                    high = mid - 1
                    

                # is right neighbour greater
                elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                    low = mid + 1

                # found peak
                else:
                    return mid
                    
        
        pIdx = binary_search(0, len(nums)-1)
        
        return pIdx
        
        
s = Solution()
print(s.findPeakElement([1]))
# print(s.findPeakElement([6,5,4,3,2,3,2]))

print(s.findPeakElement([1,2,3,1]))