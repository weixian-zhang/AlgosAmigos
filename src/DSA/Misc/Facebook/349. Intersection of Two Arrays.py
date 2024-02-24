# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        result = set()
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        N1 = len(nums1)
        N2 = len(nums2)
        i, j = 0, 0

        for i in range(N1):
            for j in range(N2):
                if nums1[i] == nums2[j]:
                    result.add(nums1[i])

        return list(result)
    

s = Solution()
# print(s.intersection([1,2,2,1], [2,2]))
print(s.intersection([4,9,5], [9,4,9,8,4]))