# 1 <= s.length, t.length <= 5 * 104
# all lower case
# no numbers

# may have different length

class Solution:

    def quick_sort(self, s) -> str:

        if len(s) <= 1:
            return s

        chars = list(s)

        # last char as pivot
        pivot = s[len(s) - 1]

        left = [x for x in chars if x < pivot]
        middle = [x for x in chars if x == pivot]
        right = [x for x in chars if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)


    def bubble_sort(self, s: str) -> None:
        l = len(s)
        chars = list(s)

        for i in range(l):
            for j in range(l):

                if chars[i] < chars[j]:
                    chars[i], chars[j] = chars[j], chars[i]

        return ''.join(chars)


    def isAnagram(self, s, t) -> bool:

        if len(s) != len(t):
            return False

        # sort both string
        s = self.quick_sort(s)
        t = self.quick_sort(t)

        for x in range(len(s)):
            if s[x] != t[x]:
                return False

        return True


s = Solution()
print(s.isAnagram('zxywabd', 'dxwyabz'))


import unittest

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # anagram car arc
    def test_anagram_car_arc(self):
        r = self.s.isAnagram('car', 'arc')
        self.assertTrue(r)

    # anagram - wdsaaw wdasaw

    # not anagram - ewaf ewff
