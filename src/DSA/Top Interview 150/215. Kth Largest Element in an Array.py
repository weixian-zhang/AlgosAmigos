from typing import List

# my solution - heap without sorting
# Runtime: 975 ms, faster than 8.51% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 27.9 MB, less than 98.94% of Python3 online submissions for Kth Largest Element in an Array.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # get last parent node which contains leaf
        lastParentIdx = (len(nums) // 2) - 1

        for x in range(lastParentIdx, -1, -1):
            self.heapify(nums, x)

        # delete top node K times
        for x in range(k-1):
            nums[0], nums[-1] = nums[-1], nums[0]
            nums.pop()

            self.heapify(nums, 0)

        return nums[0]
    
        

    def heapify(self, nums: List[int], idx: int):

        N = len(nums)
        largest = idx

        leftChild = (2 * idx) + 1
        rightChild = (2 * idx) + 2

        if leftChild < N and nums[leftChild] > nums[largest]:
            largest = leftChild

        if rightChild < N and nums[rightChild] > nums[largest]:
            largest = rightChild

        if largest != idx:
            nums[idx], nums[largest] = nums[largest], nums[idx]
            self.heapify(nums, largest)


s = Solution()
print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 3))
# print(s.findKthLargest([3,2,1,5,6,4], 2))