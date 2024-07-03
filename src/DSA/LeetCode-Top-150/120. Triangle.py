
from typing import List

class Solution:

    
    # recursion + memoization
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = {}

        def dfs(row, col, minSum, memo):
            
            if row >= len(triangle):
                return 0
            
            if (row,col) in dp:
                return dp[(row, col)]

            currNum = triangle[row][col]

            adjLeft = dfs(row + 1, col, minSum, memo)

            adjRight = dfs(row + 1, col + 1, minSum, memo)

            minSum += currNum + min(adjLeft, adjRight)
                                        
            dp[(row, col)] = minSum

            return minSum
            

        minSum = dfs(0, 0, 0, {})

        return minSum
    

    # dynamic programming
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [0] * (len(triangle[-1]) + 1)

        for row in triangle[::-1]:
            for idx, val in enumerate(row):
                dp[idx] = val + min(dp[idx], dp[idx + 1]) # adjacent numbers

        return dp[0]


s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))