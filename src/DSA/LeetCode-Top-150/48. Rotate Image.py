class Solution:
    
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def _swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        
        self.transpose(matrix)
        
        # then swap each row array in reverse order
        for x in range(len(matrix)):
            i = 0
            j = len(matrix[x]) - 1
            while i <= j:
                _swap(matrix[x], i, j)
                i += 1
                j -= 1
                   
    def transpose(self, matrix: list[list[int]]):
        
        # avoid last row, hence -1
        for i in range(0, len(matrix)-1):
            #avoid first number, hence starts at 1
            for j in range(i + 1, len(matrix)):
                
                # avoid digagonal line running across left to right 1,1 2,2 3,3 4,4
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    
    def rotate_with_extra_space(self,  matrix: list[list[int]]):
    
        tempMatrix = [0 for x in matrix]
        for x in range(len(matrix)):
            tempMatrix[x] = [0 for x in matrix[x]]
        
        N = len(matrix)

        for i in range(N):
            for j in range(N):
                tempMatrix[j][N - 1 - i] = matrix[i][j]
        
        return tempMatrix               
    
    def print_by_row(self, matrix):
        
        for i in range(len(matrix)):
            output = ''
            for j in range(len(matrix)):
                output += str(matrix[i][j])
            print(output)
        
        
    def print_by_col(self, matrix):
        for i in range(len(matrix)):
            output = ''
            for j in range(len(matrix)):
                output += str(matrix[j][i])
            print(output)
                
                
    
if __name__ == '__main__':
    
    s = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]#[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] #[[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
    s.print_by_row(matrix)
    # rotate90 = s.rotate_with_extra_space(matrix)
    # s.print_by_row(matrix)
    # s.print_by_col(matrix)
    
    #s.transpose(matrix)