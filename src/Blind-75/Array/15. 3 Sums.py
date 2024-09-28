from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums) - 1
        
        result = []

        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n

            while i <= left and left < right:

                threeSums = nums[i] + nums[left] + nums[right]

                if threeSums > 0:
                    right -= 1
                elif threeSums < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
    
    # brute force - Time Limit Exceeded
    # def threeSum(self, nums: List[int]) -> List[List[int]]:

    #     nums.sort()
    #     result = set()
    #     n = len(nums)

    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             for k in range(j + 1, n):
    #                 if (nums[i] + nums[j] + nums[k] == 0) and i < j and j < k:
    #                     result.add((nums[i], nums[j], nums[k]))


    #     result = [list(x) for x in result]

    #     return result

    # hash map solution - O(n2) - time limit exceeded
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = set()
        n = len(nums)
        map = {}
        for i, num in enumerate(nums):
            map[num] = i

        for i in range(n):
            for j in range(i + 1, n):

                #x = - 0 - nums[j] - nums[i] 
                missing_num_in_map = - 0 - nums[i] - nums[j]

                if (missing_num_in_map + nums[i] + nums[j] == 0 and missing_num_in_map in map and
                    map[missing_num_in_map] != i and  map[missing_num_in_map] != j):
                    result.add(tuple(sorted([nums[i], nums[j] , missing_num_in_map])))

        return result




s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([0,0,0]))
print(s.threeSum([0,0,0, 0]))