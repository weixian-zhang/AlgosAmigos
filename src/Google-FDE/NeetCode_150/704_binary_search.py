

class Solution:

    def search(self, nums: list[int], target: int) -> int:

        l = len(nums)
        low = 0
        mid = l- 1 // 2
        high = l

        while low <= high:

            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


s = Solution()
r = s.search([-1,0,3,5,9,12], 9)
print(r)


import unittest

class TestSolution(unittest.TestCase):

    # -1,0,3,5,9,12
    def test_5(self):
        s = Solution()
        r = s.search([-1,0,3,5,9,12], 5)
        self.assertEqual(r, 3)

    # -1,0,3,5,9,12
    def test_m1(self):
        s = Solution()
        r = s.search([-1,0,3,5,9,12], -1)
        self.assertEqual(r, 0)


    # -1,0,3,5,9,12
    def test_12(self):
        s = Solution()
        r = s.search([-1,0,3,5,9,12], 12)
        self.assertEqual(r, 5)

