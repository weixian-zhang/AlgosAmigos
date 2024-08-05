from typing import List

class Solution:

    # recursion + memoization
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        Rows = len(obstacleGrid)
        Cols = len(obstacleGrid[0])
        dp = {}

        def dfs(row, col, paths) -> int:

            # hit obstacle or our of bounds
            if row > Rows - 1 or col > Cols - 1 or obstacleGrid[row][col] == 1:
                return 0
            
            if row == Rows - 1 and col == Cols - 1:
                return 1
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            # down = dfs(row + 1, col, paths)

            # right = dfs(row, col + 1, paths)

            # paths += down + right

            # dp[(row, col)] = paths

            # code simplify to

            dp[(row, col)] = dfs(row + 1, col, paths) + dfs(row, col + 1, paths)

            return dp[(row, col)] 
        

        return dfs(0, 0, 0)
    
    # true dp
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
            
            Rows = len(obstacleGrid)
            Cols = len(obstacleGrid[0])

            dp = [[0] * (Cols + 1) for j in range(Rows + 1)]

            dp[Rows - 1][Cols - 1] = 1

            # mark obstacles in dp
            for i in range(Rows):
                 for j in range(Cols):
                      if i <= Rows -1 and j <=Cols -1 and obstacleGrid[i][j] == 1:
                           dp[i][j] = float('inf')


            for i in range(Rows - 1, -1, -1):
                 for j in range(Cols - 1, -1, -1):

                    if dp[i][j] == float('inf'):
                      continue

                    down = dp[i + 1][j] if dp[i + 1][j] != float('inf') else 0

                    right = dp[i][j + 1] if dp[i][j + 1] != float('inf') else 0  

                    dp[i][j] = dp[i][j] + down + right

            return dp[0][0] 
            



s = Solution()

#print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(s.uniquePathsWithObstacles([[0,1],[0,0]]))
print(s.uniquePathsWithObstacles([[0,1],[1,0]]))