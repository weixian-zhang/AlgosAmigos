
# 2 <= nums.length <= 10^4
# Only one valid answer exists.

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
   
         diff = {}

         for x in range(len(nums)):
            curr = nums[x]
            d = target - curr
            if not curr in diff:
                diff[d] = x
            else:
                return [x, diff[curr]]