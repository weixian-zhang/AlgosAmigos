from typing import List

# my solution
# Runtime: 42 ms, faster than 21.84% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 16.6 MB, less than 59.05% of Python3 online submissions for Spiral Matrix
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        i, j = 0, 0
        R = len(matrix)
        C = len(matrix[0])
        result = []
        topBound, rightBound, bottomBound, leftBound = 0, C-1, R-1, 0
        visited = []

        while len(visited) < (R * C):
        
            # move right
            while j <= rightBound and (i,j) not in visited:
                #if (i,j) not in visited:
                result.append(matrix[i][j])
                visited.append((i,j))
                
                j = (j + 1) if j + 1 <= rightBound else j

            rightBound -= 1
            i = (i + 1) if i + 1 <= bottomBound else i

            # move down
            while i <= bottomBound and (i,j) not in visited:
                #if (i,j) not in visited:
                result.append(matrix[i][j])
                visited.append((i,j))
                
                i = (i + 1) if i + 1 <= bottomBound else i

            topBound += 1
            bottomBound -= 1
            j = (j - 1) if (j-1) >= leftBound else j

            # move left
            while j >= leftBound and (i,j) not in visited:
                #if (i,j) not in visited:
                result.append(matrix[i][j])
                visited.append((i,j))
                j = (j - 1) if (j-1) >= leftBound else j


            leftBound += 1
            i = (i - 1) if (i-1) >= topBound else i

            # move up
            while i >= topBound and (i,j) not in visited:
                #if (i,j) not in visited:
                result.append(matrix[i][j])
                visited.append((i,j))
                i = (i - 1) if (i-1) >= topBound else i

            
            j = (j + 1) if j + 1 <= rightBound else j

        return result
    

# official solution, reference as code is much shorter
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result






s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))