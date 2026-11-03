# 1 <= s1.length, s2.length <= 104

from collections import Counter

class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()

        for right in range(len(s2)):
            window[s2[right]] += 1          # letter comes in

            left = right - len(s1)
            if left >= 0:
                window[s2[left]] -= 1       # letter goes out

            # Counter can compare to counter.
            # Don't have to sum(.values()
            if window == need:
                return True

        return False

    def create_empty_tracker(self, s: str):
        c = Counter(s)
        for k in c:
            c[k] = 0
        return c

    def _checkInclusion(self, s1: str, s2: str) -> bool:

        s1_len = len(s1)
        s1_tracker = Counter(s1)
        s2_size = len(s2)
        s2_chars = list(s2)

        left = 0

        while left <= s2_size - 1:

            left_char = s2[left]
            if left_char not in s1_tracker:
                left += 1
                continue

            # has substring

            right = left
            while (right <= s2_size - 1 and 
                   s2_chars[right] in s1_tracker and
                   s1_tracker[s2[right]] > 0):
                right_char = s2_chars[right]
                s1_tracker[right_char] -= 1
                right += 1

            # is all S1 substring is in S2. 
            if sum(s1_tracker.values()) == 0:
                return True

            #reset tracker
            s1_tracker = Counter(s1)

            left += 1

        return False


s = Solution()
#print(s.checkInclusion('adc', 'dcda')) # true
# print(s.checkInclusion('hello', 'ooolleoooleh')) # false
print(s.checkInclusion('ab', 'eidbaooo'))# true
#print(s.checkInclusion('ab', 'eidboaoo')) # false

