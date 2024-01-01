from typing import List

class Solution:

    # brite force TLE
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        minSum = float('inf')
        R = len(grid) - 1
        C = len(grid[0]) - 1

        def dfs(row, col, tempSum):
            nonlocal minSum

            if row > R or col > C:
                return float('inf')
            
            tempSum += grid[row][col]

            if row == R and col == C:
                minSum = min(minSum, tempSum)
                return 

            dfs(row + 1, col, tempSum)

            dfs(row, col + 1, tempSum)


        dfs(0, 0, 0)

        return minSum




s= Solution()
# print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(s.minPathSum([[1,2,3],[4,5,6]]))