# 33. Search in Rotated Sorted Array

from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        N = len(nums)

        def binary_search(nums: List[int], target: int, low:int, high: int):
            
            l = low
            h = high
            
            while l <= h:
                
                mid = (h + l) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    h = mid - 1
                else:
                    l = mid + 1

            return -1
        
        
        if nums[0] < nums[-1]:
            return binary_search(nums, target, 0, N -1)


        # find the pivot index where array is rotated
        pivotIdx = 0
        
        for idx, x in enumerate(nums):
            nextIdx = idx + 1 if idx + 1 <= N-1 else idx
            if x > nums[nextIdx]:
                pivotIdx = nextIdx
                break

        result = binary_search(nums, target, pivotIdx, N - 1)
        return result if result != -1 else binary_search(nums, target, 0, pivotIdx - 1)

        

s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
print(s.search([4,5,6,7,0,1,2], 3))
print(s.search([1,2,3,4,5,6,7,8], 5))

        
