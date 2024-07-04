from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        R = len(grid) - 1
        C = len(grid[0]) - 1

        minSum = float('inf')

        def dfs(row, col, localSum):
            nonlocal minSum
            
            if row > R or col > C:
                return
            
            if row == R and col == C:
                localSum += grid[row][col]
                minSum = min(minSum, localSum)
                return
            

            localSum += grid[row][col]
            
            dfs(row + 1, col, localSum)

            dfs(row, col + 1, localSum)

            localSum -= grid[row][col] # backtracking


        dfs(0, 0, 0)

        return minSum


s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))