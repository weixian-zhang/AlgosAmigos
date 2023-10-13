class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        subsequenceIdxes = []
        
        marker, finder = 0, 0
        for sub in s:
            
            while finder <= len(t)-1:
                
                if sub == t[finder]:
                    marker = finder
                    finder += 1
                    subsequenceIdxes.append(marker)
                    break
                else:
                    finder += 1
                
        return len(subsequenceIdxes) == len(s)
            
            
if __name__ == '__main__':
    s = Solution()
    #s.isSubsequence('abc', 'ahbgdc')
    s.isSubsequence('axc','ahbgdc')