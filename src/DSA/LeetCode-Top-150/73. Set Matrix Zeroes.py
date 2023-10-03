class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix) == 0:
            return
        
        colLen = len(matrix[0])
        
        zeroLocations = self.find_all_zeros(matrix)
        
        for x in range(len(zeroLocations)):
            row, col = zeroLocations[x][0], zeroLocations[x][1]
            self.set_row_zero(matrix, row)
            self.set_col_up_zero(matrix, row, col)
            self.set_col_down_zero(matrix, row, col)
    
    def find_all_zeros(self, matrix):
        zeroLocations = []
        colLen = len(matrix[0])
        
        for row in range(len(matrix)):
            for col in range(colLen):
                if matrix[row][col] == 0:
                    zeroLocations.append([row, col])
        return zeroLocations
    
    def set_row_zero(self, matrix: list[list[int]], row: int):

        for x in range(len(matrix[row])):
            matrix[row][x] = 0
    
    def set_col_up_zero(self, matrix: list[list[int]], row: int, col: int):
        
        while row > 0:
            row -= 1
            matrix[row][col] = 0
            
    
    def set_col_down_zero(self, matrix: list[list[int]], row: int, col: int):
        while row <= len(matrix)-1:
            matrix[row][col] = 0
            row += 1
        
        
if __name__ == '__main__':
    s = Solution()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    print(matrix)