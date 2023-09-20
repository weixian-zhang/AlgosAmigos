class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram(s="rat", t="car"))
        
        