
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # O(n) + O(log n)

        l = len(numbers)

        def binary_search(nums, target):
            low = 0
            high = len(nums) - 1

            while low <= high:

                mid = (high + low) // 2

                if nums[mid] == target:
                    return mid

                if target > nums[mid]:
                    low = mid + 1
                
                if target < nums[mid]:
                    high = mid - 1
            
            return -1
        
        for x in range(l):

           new_target = target - numbers[x]
           search_idx = binary_search(numbers[x+1:], new_target)

           if search_idx == -1:
                continue
           
           idx_1 = x + 1
           idx_2 = idx_1 + (search_idx + 1)

           return [idx_1, idx_2]


        # O(n^2) - works but time limit exceeded
        size = len(numbers)
        for i in range(size):
            for j in range(1, size):

                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]


# s = Solution()
# print(s.twoSum([2,7,11,15], 9))
# print(s.twoSum([-1,0], -1))
# print(s.twoSum([2,3,4], 6))


import unittest
class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # [2,7,11,15,18,20,22], 44
    def test_1(self):
        result = self.s.twoSum([2,7,11,15,18,20,22], 44)
        self.assertTrue(6, result[0])
        self.assertTrue(7, result[1])


    # [2,4], 6

    # [-1,0], -1