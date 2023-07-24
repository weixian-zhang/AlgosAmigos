

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text1) == 0 or len(text2) == 0:
            return 0
        
        if len(text1) == 1 and len(text2) == 1 and text1[0] == text2[0]:
            return 1
        
        if len(text1) == 2 and len(text2) == 2 and text1[0] == text2[0]:
            return 2
        
        if text1 == text2:
            return len(text1)
        
        t1Len = len(text1)
        t2Len = len(text2)
        
        dp = [0 for i in range(t1Len + 1)]
        for i in range(t1Len + 1):
            dp[i] = [0 for j in range(t2Len + 1)]
        
        for i in range(t1Len + 1):
            for j in range(t2Len + 1):
                
                if i == 0 or j == 0:
                    continue
                elif text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i-1][j-1] 
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[t1Len][t2Len]
        
        
        
if __name__ == '__main__':
    s = Solution()
    
    r = s.longestCommonSubsequence('abcde', 'ace')
    
    print(r)