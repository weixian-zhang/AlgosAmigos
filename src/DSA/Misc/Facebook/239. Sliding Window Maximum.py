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

# neetcode solution - monotonic decreasing queue    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        dq = deque()
        leftIdx, right = 0, 0

        # continue with "second part" which is rest of numbers after first window K
        while right < len(nums):
            
            # pop smaller num in queue, no point consider smaller nums when bigger num appears
            while dq and nums[right] >= nums[dq[-1]]:
                dq.pop()

            dq.append(right)

            # remove/ignore prev window item as leftIdx progress
            if leftIdx > dq[0]:
                dq.popleft() 

            # only when first window is reach then start to add number to result
            if (right + 1) >= k:
                result.append(nums[dq[0]])
                leftIdx += 1

            right += 1

        return result
    
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         dq = deque()
#         res = []

#         for i in range(k):
#             while dq and nums[i] >= nums[dq[-1]]:
#                 dq.pop()
#             dq.append(i)

#         res.append(nums[dq[0]])

#         for i in range(k, len(nums)):
#             if dq and dq[0] == i - k:
#                 dq.popleft()
#             while dq and nums[i] >= nums[dq[-1]]:
#                 dq.pop()

#             dq.append(i)
#             res.append(nums[dq[0]])

#         return res


s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(s.maxSlidingWindow([1], 1))