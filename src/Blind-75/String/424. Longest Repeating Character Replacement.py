from collections import defaultdict

class Solution:
    
    def characterReplacement(self, s: str, k: int) -> int:

        longest = 0
        l = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)

            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] = counts[s[l]] - 1
                l += 1

            longest = max(longest, r - l + 1)


        return longest


        