from typing import List

class Solution:

    # O(n log n) for merge sort
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        mergedArr = nums1 + nums2

        mergedArr.sort()

        if len(mergedArr) % 2 == 0:
            idx1 = len(mergedArr) // 2
            idx2 = idx1 - 1
            return (mergedArr[idx1] + mergedArr[idx2]) / 2
        else:
            idx = len(mergedArr) // 2
            return mergedArr[idx]



s = Solution()
print(s.findMedianSortedArrays([1,3], [2]))
print(s.findMedianSortedArrays([1,2], [3,4]))