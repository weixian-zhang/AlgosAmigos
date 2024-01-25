from typing import List

# my solution - 2 pointer approach
# Runtime: 46 ms, faster than 55.92% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 16.9 MB, less than 58.63% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
class Solution:

    
    def findMin(self, nums: List[int]) -> int:
        
        # no rotation
        if nums[0] <= nums[-1]:
            return nums[0]
        
        N = len(nums)

        def two_pointers():
            
            left, right = 0, N - 1

            while left + 1 != right:

                if nums[left] < nums[left + 1]:
                    left += 1

                if nums[right] > nums[right - 1]:
                    right -= 1

                    
            return nums[left + 1]

        result = two_pointers()

        return result
    
# neetcode solution - modified binary search    
# Runtime: 45 ms, faster than 61.16% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 16.8 MB, less than 67.75% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
class Solution:

    
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]
        
        N = len(nums)
        left, right = 0, N - 1

        smallest = nums[0]

        def binary_search(left, right):
            nonlocal smallest

            while left <= right:

                mid = (right + left) // 2

                smallest = min(smallest, nums[mid])

                # mid is in left portion
                if nums[mid] >= nums[0]: 
                    left = mid + 1

                # mid is in right portion, where small numbers are
                elif nums[mid] < nums[0]:
                    right = mid - 1
                 
                
            return smallest
            
        return binary_search(left, right)

s = Solution()
print(s.findMin([3,4,5,1,2]))
# print(s.findMin([4,5,1,2,3]))
# print(s.findMin([1]))
# print(s.findMin([4,5,6,7,0,1,2]))
# print(s.findMin([11,13,15,17]))