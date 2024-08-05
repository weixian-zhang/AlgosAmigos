class Solution:
    
    # solution using sliding window
    def strStr(self, haystack: str, needle: str) -> int:
        
        sliding_window_size = len(needle)
        
        for i in range(len(haystack) - (sliding_window_size-1)): # -1 at sliding window to handle 0 index
            
            if haystack[i: i + sliding_window_size] == needle:
                return i
            
        return -1
        
    
    
    
if __name__ == '__main__':
    s = Solution()
    #s.strStr('sadbutsad', 'sad')
    s.strStr('leetcode', 'leeto')