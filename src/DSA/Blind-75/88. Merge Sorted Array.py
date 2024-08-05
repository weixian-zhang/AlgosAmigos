from typing import List

class Solution:
    
    # offical solution
    # 33ms Beats 91.19%
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        last = m + n - 1
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            if nums2[n] > nums1[m]:
                nums1[last] = nums2[n]
                n -= 1
            else:
                nums1[last] = nums1[m]
                m -= 1
            
            last -= 1

        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1

    
    # my solution - pop excess and merge
    # 38ms Beats 69.82%
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        while len(nums1) > m:
            nums1.pop()

        nums1 += nums2
        nums1.sort()




s = Solution()

#print(s.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(s.merge([0], 0, [1], 1))
#print(s.merge([1], 1, [], 0))


            