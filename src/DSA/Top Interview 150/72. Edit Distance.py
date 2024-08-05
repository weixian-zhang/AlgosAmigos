class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if len(word1) == 0 or len(word2) == 0: return len(word1) or len(word2)
    
        dp = {}

        def dfs(i, j):
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i == len(word1): return len(word2) - j
            
            if j == len(word2): return len(word1) - i
            
            opsI, opsR, opsD = 0, 0, 0

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                # insert
                opsI = 1 +  dfs(i, j + 1) #dfs(insertAt(, i, j), i, j + 1)

                # replace
                opsR = 1 + dfs(i + 1, j + 1) #dfs(w1.replace(w1[i], word2[j], 1), i + 1, j + 1)

                # delete
                opsD = 1 + dfs(i + 1, j) #dfs(w1.replace(w1[i], '', 1), i + 1, j)

                dp[(i, j)] = min(opsI, opsR, opsD)

                return dp[(i, j)]

        return dfs(0, 0)
    
#            2
#        a   c   d
#     a inf inf inf 3
#   1 b inf inf  1 2
#     d  2   1   0  1
#        3   2   1  0

    def minDistance(self, word1: str, word2: str) -> int:
        
        dp = [[ (float('inf')) for x in range(len(word2) + 1)] for i in range(len(word1) + 1)]

        # init last column
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i #len(word1) - i if len(word1) - i >= 0 else 0

        # init last row
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j # len(word1) - j if len(word1) - j >= 0 else 0

        #dp[len(word1)-1][len(word2)-1] = 0

        # actual dp
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1])

        return dp[0][0]
    


s = Solution()
print(s.minDistance('', 'a'))
#print(s.minDistance('intention', 'execution'))
# print(s.minDistance('horse', 'ros'))
#print(s.minDistance('abd', 'acd'))