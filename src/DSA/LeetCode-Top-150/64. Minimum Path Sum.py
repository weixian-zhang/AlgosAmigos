from typing import List

class Solution:
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



s = Solution()

print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))