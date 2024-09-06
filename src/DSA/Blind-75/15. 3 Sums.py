from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums) - 1
        i, j, k = 0, 1, n
        result = []
        r_idx = []
        nums.sort()

        while i <= k and j <= k:

            if k == j:
                k = n
                i += 1
                j += 1
                continue

            if (nums[i] + nums[j] + nums[k] == 0) and i < j and j < k:
                result.append((nums[i], nums[j], nums[k]))

   
            k -= 1

            new_result = [list(y) for y in set(result)]

        return new_result
    
    # brute force - Time Limit Exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    if (nums[i] + nums[j] + nums[k] == 0) and i < j and j < k:
                        result.add((nums[i], nums[j], nums[k]))


        result = [list(x) for x in result]

        return result




s = Solution()
# print(s.threeSum([-1,0,1,2,-1,-4]))
# print(s.threeSum([0,1,1]))
# print(s.threeSum([0,0,0]))
print(s.threeSum([0,0,0, 0]))