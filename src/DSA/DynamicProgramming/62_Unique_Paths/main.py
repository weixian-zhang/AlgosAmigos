class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        matrix = [0 for i in range(m)]
        for idx, val in enumerate(matrix):
            matrix[idx] = [0 for i in range(n)]
            
        # initialize destination cell to 1
        matrix[m-1][n-1] = 1
        
        memoization = {}
        
        paths = self.upRecurse(matrix, 0, 0, memoization)
        
        return paths
    
    
    def upRecurse(self, matrix, row, col, memoization) -> int:
        rowLimit = len(matrix) - 1
        colLimit = len(matrix[0]) - 1
        
        
        # destination cell
        if (row, col) in memoization:
            return memoization[(row,col)]
        
        elif row == rowLimit or col >= colLimit:
            return 1
        
        elif row >= rowLimit:
            return 1 + self.upRecurse(matrix, row, col + 1, memoization)

        elif col >= colLimit:
            return 1 + self.upRecurse(matrix, row + 1, col, memoization)
        
        else:
            memoization[(row, col)]  = self.upRecurse(matrix, row + 1, col, memoization) + self.upRecurse(matrix, row, col+1, memoization)
            return memoization[(row, col)]



if __name__ == '__main__':
    
    sol = Solution()
    paths = sol.uniquePaths(m=3, n=7)
    print(paths)