from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[-1] >= nums[0]:
            return nums[0]
        
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (right + left) // 2

            if left == right: #nums[mid] <= nums[right] and nums[mid] <= nums[left]:
                return nums[mid]
            elif nums[mid] > nums[right]: # small numbers on right side due to rotation
                left = mid + 1
            else:
                right = mid


s = Solution()

print(s.findMin([5,1,2,3,4]))
# print(s.findMin([2,1]))

# print(s.findMin([3,4,5,1,2]))
# print(s.findMin([0,1,2,4,5,6,7]))
# print(s.findMin([1,2,3,4,5]))