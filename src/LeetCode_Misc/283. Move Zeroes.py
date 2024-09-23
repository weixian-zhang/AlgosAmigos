from typing import List

class Solution:
    # solve with 2 loops
    # Runtime: 134 ms, faster than 32.07% of Python3 online submissions for Move Zeroes.
    # Memory Usage: 17.9 MB, less than 99.53% of Python3 online submissions for Move Zeroes.
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return
        
        numOfZeros = 0

        for x in nums:
            if x == 0:
                numOfZeros += 1

        x = 0
        while x < len(nums):
            if nums[x] == 0:
                nums.pop(x)
                continue
            x += 1
        
        nums + [0 for x in range(numOfZeros)]

    # Runtime: 121 ms, faster than 82.86% of Python3 online submissions for Move Zeroes.
    # Memory Usage: 18.1 MB, less than 31.36% of Python3 online submissions for Move Zeroes.
    def moveZeroes(self, nums: List[int]) -> None:

        if len(nums) == 1:
            return

        left, right = 0, 0

        while right < len(nums):
            # keep swapping non zeros to the front
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

                
         

s = Solution()
print(s.moveZeroes([0,1,0,3,12]))
            
        
        