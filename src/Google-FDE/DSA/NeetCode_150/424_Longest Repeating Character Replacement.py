from collections import Counter

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        max_len = 0

        for right in range(len(s)):
            counts[s[right]] += 1

            window_length = right - left + 1
            keep = max(counts.values())
            letters_to_change = window_length - keep

            # Shrink the window until it needs k changes or fewer
            # all letters - letters you keep, left with N letters to change.
            while letters_to_change > k:
                counts[s[left]] -= 1
                left += 1
                window_length = right - left + 1
                keep = max(counts.values())
                letters_to_change = window_length - keep

            max_len = max(max_len, right - left + 1)

        return max_len



    def _characterReplacement(self, s: str, k: int):

        chars = list(s)
        size = len(s) - 1
        swap = k
        max_len = 0
        left = right = 0

        # left to right
        while right <= size:

            left_char = chars[left]
            
            while swap >= 0 and right <= size:

                right_char = chars[right]

                if right_char == left_char:
                    right += 1
                else:
                    if swap > 0:
                        chars[right] = left_char
                    swap -= 1

            # reset for next run
            max_len = max(right - left, max_len)
            chars = list(s)
            left += 1
            right = left
            swap = k
        
        # right to left

        chars = list(s)
        left = right = size
        swap = k

        while left >= 0:

            right_char = chars[right]

            while swap >= 0 and left >= 0:

                left_char = chars[left]

                if left_char == right_char:
                    left -= 1
                else:
                    if swap > 0:
                        chars[left] = right_char
                    swap -=1

            # reset for next run
            max_len = max(right - left, max_len)
            chars = list(s)
            right -= 1
            left = left
            swap = k
        
        return max_len


s = Solution()
print(s.characterReplacement('ABBB', 2))
# print(s.characterReplacement('B', 2))
print(s.characterReplacement('AABABBA', 1))
print(s.characterReplacement('ABAB', 2))



class TestSolution():
    pass

    # A - one char

    

