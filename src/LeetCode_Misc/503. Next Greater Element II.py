from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        minNum = -10**10
        result = [minNum] * len(nums)
        mstack = []

        # loop left to right
        for i in range(len(nums)):
            if not mstack:
                mstack.append((nums[i], i))
                continue

            # check if current num is larger than stack nums
            j = len(mstack) - 1
            while j >= 0 and mstack and nums[i] > mstack[j][0]:
                ng = nums[i]
                prev_num, prev_idx = mstack[j]

                if result[prev_idx] == minNum:
                    result[prev_idx] = ng
                j -= 1

            mstack.append((nums[i], i))

        if not mstack:
            return result

        # loop right to left
        for i in range(len(nums) - 1, -1, -1):

            if result[i] != minNum:
                continue

            while mstack and mstack[0][0] <= nums[i]:
                mstack.pop(0)

            if mstack and mstack[0][0] > nums[i]:
                ng =  mstack[0][0]
                result[i] = ng

        for i in range(len(result)):
            if result[i] == minNum:
                result[i] = -1

            
        return result
        