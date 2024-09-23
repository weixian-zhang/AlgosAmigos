class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        wordmap = {}
        
        for s in magazine:
            if s not in wordmap:
                wordmap[s] = 1
            else:
                wordmap[s] += 1
                
        for r in ransomNote:
            if r in wordmap:
                wordmap[r] -= 1
                if wordmap[r] < 0:
                    return False
            else:
                return False
        
        return True
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('aa', 'aab'))