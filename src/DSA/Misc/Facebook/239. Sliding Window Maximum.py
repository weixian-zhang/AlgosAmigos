# https://leetcode.com/problems/sliding-window-maximum/

from typing import List
from collections import deque

# brute force - Time Limit Exceeded
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        N = len(nums)
        result = []
        queue = deque([])

        for i in range(len(nums)):
            if i + k <= N:
                queue.append(i)

        while queue:
            winStartIdx = queue.popleft()
            newNum = nums[winStartIdx: winStartIdx + k]
            newNum.sort()
            result.append(newNum[-1])

        return result
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        nums.sort()
         
        N = len(nums)
        result = []
        queue = deque([])
        left = right = 0



        return result


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.maxSlidingWindow([1], 1))