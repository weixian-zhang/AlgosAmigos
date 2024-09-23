from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # O(n)
        nums1_map = {val:idx for idx, val in enumerate(nums1)}
        stack =[]
        result = [-1] * len(nums1)

        for i in range(len(nums2)):

            num = nums2[i]

            if not stack:
                stack.append(num)
                continue

            # update result
            while stack and num > stack[-1]:
                ng = stack.pop()
                if ng in nums1_map:
                    idx = nums1_map[ng]
                    result[idx] = num

            stack.append(num)

        return result


        # O(m * n)
        # for i in range(len(nums1)):
        #     idx = nums2.index(nums1[i])
        #     for j in range(idx+1, len(nums2)):
        #         if nums2[j] > nums1[i]:
        #             result[i] = nums2[j]
        #             break

        # return result
                
        