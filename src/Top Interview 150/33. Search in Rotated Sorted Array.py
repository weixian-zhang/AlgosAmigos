from typing import List

# my solution
# Runtime: 46 ms, faster than 60.37% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 16.9 MB, less than 63.55% of Python3 online submissions for Search in Rotated Sorted Array.
class Solution:

    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        
        N = len(nums)

        # normal binary search
        def binary_search(nums: list[int], low: int, high: int):

            # search left part
            while low <= high:

                mid = (high + low) // 2
                
                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return -1
        
        # find rotation/pivot index using 2 pointers
        def find_rotation_point():

            left, right = 0, N - 1

            if len(nums) == 2:
                return 0

            while left + 1 != right:

                if nums[left] < nums[left + 1]:
                    left += 1
                
                if nums[right] > nums[right - 1]:
                    right -= 1

            return left + 1
                
                    
        # has rotation
        if nums[0] < nums[-1]:
            return binary_search(nums, 0, N - 1)
        else:

            rotationIdx = find_rotation_point()

            if nums[rotationIdx] == target:
                return rotationIdx

            leftFound = binary_search(nums, 0, rotationIdx)

            if leftFound != -1:
                return leftFound
            else:
                return binary_search(nums, rotationIdx + 1, N - 1)

            
        
        

        

s = Solution()
# print(s.search([4,5,6,7,8,1,2,3], 8))
print(s.search([5,1,3], 1))
# print(s.search([1,2,3,4,5,6,7,8,9], 1))
# print(s.search([3,5,1], 1))
# print(s.search([3,1], 1))
# print(s.search([1], 0))
# print(s.search([4,5,6,7,0,1,2], 4))
# print(s.search([4,5,6,7,0,1,2], 3))
