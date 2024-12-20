from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        N = len(nums)
        l, r = 0, N - 1

        while l <= r:

            mid = (r + l) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return -1

        
        