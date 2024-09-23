from typing import List

class Solution:

    # extra space Set
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueVals = set([])

        for n in nums:
            if n in uniqueVals:
                return True
            else:
                uniqueVals.add(n)

        return False
    

    # no extra O(n) space
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums.sort()
        N = len(nums)
        left, right = 0, 1

        while not left >= N and not right >= N:

            if nums[left] == nums[right]:
                return True
            
            left += 1
            right += 1
            
        return False
    

s = Solution()
print(s.containsDuplicate([1,2,3,4]))
print(s.containsDuplicate([1,2,3,1]))
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))


        