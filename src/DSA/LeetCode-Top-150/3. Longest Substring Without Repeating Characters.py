class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest = 0
        nonRepeatingTracker = []

        i = 0
        for i in range(len(s)):
            if s[i] not in nonRepeatingTracker:
                nonRepeatingTracker.append(s[i])
                
            else:
                longest = max(len(nonRepeatingTracker), longest)

                idx = nonRepeatingTracker.index(s[i])

                nonRepeatingTracker = nonRepeatingTracker[idx+1:]

                nonRepeatingTracker.append(s[i])

        longest = max(len(nonRepeatingTracker), longest)
        return longest

s = Solution()
print(s.lengthOfLongestSubstring(' '))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('pwwkew'))
print(s.lengthOfLongestSubstring('dvdb'))