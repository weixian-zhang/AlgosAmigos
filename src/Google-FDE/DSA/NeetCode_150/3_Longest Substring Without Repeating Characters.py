# 0 <= s.length <= 10^5

from collections import Counter

class Solution:

    def has_dup(self, s, start, end):
        current_str = s[start:end+1]
        r = len(set(current_str)) != len(current_str)
        return r

    # leetcode solution
    def _lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[r] += 1

            while chars[r] > 1:
                l = s[left]
                chars[l] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res


    def lengthOfLongestSubstring(self, s: str):

        size = len(s) - 1
        chars = Counter()
        left = right = 0
        max_len = 0

        while right <= size:

            curr_char = s[right]

            chars[curr_char] += 1

            while chars[curr_char] > 1:
                # reduce char count as left is about to move forward
                left_char = s[left]
                chars[left_char] -= 1

                left += 1

            max_len = max(right - left + 1, max_len)

            right += 1

        return max_len
    
        # if len(s) == 0: # to merge to below logic
        #     return 0

        # size = len(s) - 1
        # last_seen_char = {}
        # max_len = 0
        # start, end = 0, 0

        # while end <= size:
        #     char = s[end]
        #     # at this point, `end` is pointing to a duplicate char
        #     # Start index have to move past the existing duplicate char.
        #     # If not, then the end is also pointing to a duplicated char. 
        #     if char in last_seen_char and last_seen_char[char] >= start:
        #         start = last_seen_char[char] + 1

        #     last_seen_char[char] = end
        #     max_len = max(end - start + 1, max_len)
        #     end += 1

        # return max_len


s = Solution()
# print(s.lengthOfLongestSubstring('1R1T7'))
# print(s.lengthOfLongestSubstring('bbbbb'))
print(s.lengthOfLongestSubstring('abcabcbb'))

import unittest

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # bbbbb = 1
    def test_bbbbb(self):
        r = self.s.lengthOfLongestSubstring('bbbbb')
        self.assertTrue(r, 1)

    # dcmepd = 5
    def test_dcmepd(self):
        r = self.s.lengthOfLongestSubstring('dcmepd')
        self.assertTrue(r, 5)


    # awsdkeptochdkor = 15
    def test_awsdkeptochdkor(self):
        r = self.s.lengthOfLongestSubstring('awsdkeptochdkor')
        self.assertTrue(r, 15)

    # '' = 0
    def test_empty_string(self):
        r = self.s.lengthOfLongestSubstring('')
        self.assertEqual(r, 0)

    # awsdkepto123chdkor = 18
    def test_awsdkepto123chdkor(self):
        r = self.s.lengthOfLongestSubstring('awsdkepto123chdkor')
        self.assertTrue(r, 18)

    # awsdkepto123chdkor3 = 18
    def test_awsdkepto123chdkor3(self):
        r = self.s.lengthOfLongestSubstring('awsdkepto123chdkor3')
        self.assertTrue(r, 18)