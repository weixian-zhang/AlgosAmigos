from typing import List

class Solution:

    # top down recursion + memoization
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        R = len(grid) - 1
        C = len(grid[0]) - 1

        dp = {}

        def dfs(row, col):

            if row > R or col > C:
                return float('inf')
            
    
            if row == R and col == C:
               return grid[row][col]
            
            if (row, col) in dp:
                return dp[(row, col)]
            
        
            currNum = grid[row][col]

            # downSum = dfs(row + 1, col, localSum)

            # rightSum = dfs(row, col + 1, localSum)

            # localSum = currNum + min(downSum, rightSum)

            # dp[(row, col)] = localSum
            
            dp[(row, col)] = currNum + min(dfs(row + 1, col), dfs(row, col + 1))

            return  dp[(row, col)]


        return dfs(0, 0, 0)
    
    # dp
    # 1,   3,   1, inf
    # 1,   5,   1, inf
    # 4,   2,   1, inf
    # inf, inf, 0, inf
    def minPathSum(self, grid: List[List[int]]) -> int:

        R = len(grid)
        C = len(grid[0])

        dp = [[0 for j in range(C + 1)] for i in range(R + 1)]

        #set outer row to infinity
        for j in range(C + 1):
            dp[R][j] = float('inf')
        
        # set outer col to infinity
        for i in range(R + 1):
            dp[i][C] = float('inf')

        dp[R][C - 1] = 0
        
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i+ 1][j], dp[i][j + 1])

        return dp[0][0]





s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))