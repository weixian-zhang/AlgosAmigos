from typing import List

# my solution
# Runtime: 79 ms, faster than 65.76% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 17.8 MB, less than 67.25% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        N = len(nums)

        def binary_search(low: int, high: int):

            while low <= high:

                mid = (high + low) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return -1
        
        firstIdx = binary_search(0, N - 1)
        leftPartIdx = -1
        rightPartIdx = -1

        if firstIdx == -1:
            return [-1, -1]
        
        # keep finding left until -1, then get the lowest/ start index
        newLeftIdx = firstIdx - 1
        while newLeftIdx <= N - 1:
            
            newLeft = binary_search(0, newLeftIdx)

            if newLeft != -1:
                leftPartIdx = newLeft
                newLeftIdx -= 1
            else:
                break

        # keep finding right until -1, then get the highest/end index
        newRightIdx = firstIdx + 1
        while newRightIdx <= N - 1:
            
            newRight = binary_search(newRightIdx, N - 1)

            if newRight != -1:
                rightPartIdx = newRight
                newRightIdx += 1
            else:
                break

        leftPartIdx = firstIdx if leftPartIdx == -1 else leftPartIdx

        rightPartIdx = firstIdx if rightPartIdx == -1 else rightPartIdx

        rightPartIdx = max(firstIdx, rightPartIdx)
            
        return [leftPartIdx, rightPartIdx]


s = Solution()
print(s.searchRange([1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8], 8))
print(s.searchRange([3,3,3], 3))
# print(s.searchRange([1,2,3,3,3,4,5,6], 3))
print(s.searchRange([1], 0))
# print(s.searchRange([1], 1))
print(s.searchRange([2, 2], 2))
# print(s.searchRange([1, 3], 1))
# print(s.searchRange([1], 1))
# print(s.searchRange([], 0))
# print(s.searchRange([5,7,7,8,8,10], 8))
# print(s.searchRange([5,7,7,8,8,10], 6))