class Solution:

        
    # def lengthOfLongestSubstring(self, s: str) -> int:
        
    #     if s == '':
    #         return 0
        
    #     longest = 0
    #     visited = {}    # stores each visited letter and its index
        
    #     left = 0
    #     right = 0
        
    #     for right in range(len(s)):
            
    #         if s[right] in visited:
    #             left = max(left, visited[s[right]]) + 1    # narrow the window, shift left to one position after duplicate
            
    #         longest = max(longest, right - left + 1)
    #         visited[s[right]]  = right
            
        
    #     return longest
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        longest = 0
        left = 0
        
        for right in range(len(s)):
            
            while s[right] in visited:
                visited.remove(s[left]) # shrink left cursor window
                left += 1
               

            visited.add(s[right])
            longest = max(longest, right - left + 1)
            
        return longest
            
    
class TestA:
    def test_longest_substring_1(s='abcabcbb'):
        s = Solution()
        lenOfLongestSubstring = s.lengthOfLongestSubstring(s)
        assert lenOfLongestSubstring == 3
        
    def test_longest_substring_2(s='bbbbb'):
        s = Solution()
        lenOfLongestSubstring = s.lengthOfLongestSubstring(s)
        assert lenOfLongestSubstring == 1
    
    
if __name__ == '__main__':
    
    s = Solution()
    lenOfLongestSubstring = s.lengthOfLongestSubstring("pwwkew") #dvdf
    print(lenOfLongestSubstring)