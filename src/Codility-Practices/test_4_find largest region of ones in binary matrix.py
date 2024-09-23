# in a 2D binary matrix where elements are either 1s or 0s
# find the largest 1s region
# e.g: largest region is 12 located in the center
# [
#  [1,0,0,0,0,0,0,0,0,0,0,0,1],
#  [0,0,0,0,0,0,0,0,0,0,0,0,0], 
#  [0,0,0,0,0,1,1,1,1,0,0,0,0], 
#  [0,0,0,0,0,1,1,1,1,0,0,0,0], 
#  [0,0,0,0,0,1,1,1,1,0,0,0,1], 
#  [0,0,0,0,0,0,0,0,0,0,0,0,0], 
#  [0,0,0,1,1,1,0,0,0,0,0,0,0],
#  [1,0,0,0,0,0,0,0,0,0,0,0,1]
#  ]
      
def find_ones(matrix: list[list]):
    
    R = len(matrix) # row bottom boundary
    C = len(matrix[0]) # col right boundary
    maxOnes = 0
    visited = set()

    def find_ones_neighbours(row, col, parent) -> list[tuple]:
        
      ones = []
      
      # up
      if row - 1 >= 0 and matrix[row - 1][col] == 1 and (row - 1, col) not in visited:
        ones.append((row - 1, col))
        
      # down
      if row + 1 <= R - 1 and matrix[row + 1][col] == 1 and (row + 1, col) not in visited:
        ones.append((row + 1, col))
        
      # left
      if col - 1 >= 0 and matrix[row][col - 1] == 1 and (row, col - 1) not in visited:
        ones.append((row, col - 1))
        
      # right
      if col + 1 <= C - 1 and matrix[row][col + 1] == 1 and (row, col + 1) not in visited:
        ones.append((row, col + 1))
        
      return ones
    
    def dfs(row, col, tempSum):
      nonlocal maxOnes

      ones = find_ones_neighbours(row, col, (row, col))

      tempSum += len(ones) 
      maxOnes = max(maxOnes, tempSum) 
      
      # mark visited to not repeat when finding neighbours
      for r, c in ones:
        visited.add((r,c))

      for r, c in ones:
        dfs(r, c, tempSum)

      return tempSum

    for row in range(R):
      for col in range(C):
        if matrix[row][col] == 0 and (row,col) not in visited:
            continue
        
        dfs(row, col, 0)
        
    return maxOnes
  
  
       
# matrix = [
#  [0,0,0,0,0,0,0,0,1,0,1,0,0], 
#  [0,0,0,0,0,0,0,0,1,1,1,0,0], 
#  [0,0,0,0,0,0,0,0,0,0,1,0,0]]

# matrix = [
#  [0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0], 
#  [0,1,1,0,1,0,0,0,0,0,0,0,0], 
#  [0,1,0,0,1,1,0,0,1,0,1,0,0], 
#  [0,1,0,0,1,1,0,0,1,1,1,0,0], 
#  [0,0,0,0,0,0,0,0,0,0,1,0,0], 
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]

matrix = [
 [1,0,0,0,0,0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0,0,0,0,0,0], 
 [0,0,0,0,0,1,1,1,1,0,0,0,0], 
 [0,0,0,0,0,1,1,1,1,0,0,0,0], 
 [0,0,0,0,0,1,1,1,1,0,0,0,1], 
 [0,0,0,0,0,0,0,0,0,0,0,0,0], 
 [0,0,0,1,1,1,0,0,0,0,0,0,0],
 [1,0,0,0,0,0,0,0,0,0,0,0,1]
 ]
 
 
print(find_ones(matrix))