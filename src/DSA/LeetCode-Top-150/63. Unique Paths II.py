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
            
            



s = Solution()

print(s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))