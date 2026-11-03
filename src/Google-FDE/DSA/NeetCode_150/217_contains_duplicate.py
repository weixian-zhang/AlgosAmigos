
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# not sorted



class Solution:

    def containsDuplicate(self, nums: list[int]) -> bool:
        # method 1
        #return len(set(nums)) < len(nums)

        #method 2

        visited = {}

        for x in nums:
            if x in visited:
                return True
            visited[x] = 0

        return False



import unittest

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # 1,3,5,0,-99
    def test_no_duplicate(self):
        r = self.s.containsDuplicate([1,2,3])
        self.assertFalse(r)


    # 5, 8,11,8,100
    def test_duplicate_5_8_11_8_100(self):
        r = self.s.containsDuplicate([5,8,11,8,100])
        self.assertTrue(r)

    # []
    def test_empty_list(self):
        r = self.s.containsDuplicate([])
        self.assertFalse(r)

    # 4,4,4,4
    def test_duplicate_4_4_4_4(self):
        r = self.s.containsDuplicate([4,4,4,4])
        self.assertTrue(r)

    # -99, 100,101,102,103,-99
    def test_duplicate_m99_100_101_102_103_m99(self):
        r = self.s.containsDuplicate([-99, 100,101,102,103,-99])
        self.assertTrue(r)
