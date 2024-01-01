from typing import List

class Solution:

    # DFS with parent to track cycle in this "undirected" grapg represented in matrix
    # Runtime: 4150 ms, faster than 5.21% of Python3 online submissions for Detect Cycles in 2D Grid.
    # Memory Usage: 116.8 MB, less than 69.27% of Python3 online submissions for Detect Cycles in 2D Grid.
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        R = len(grid) - 1      # row bottom boundary
        C = len(grid[0]) - 1   # column right boundary

        def get_neighbours(row, col, parent, val: str) -> list[tuple]:
            
            neighbours = []
            # up
            if row - 1 >= 0 and grid[row - 1][col] == val and (row - 1, col) != parent:
                neighbours.append((row - 1, col))

            # down
            if row + 1 <= R and grid[row + 1][col] == val and (row + 1, col) != parent:
                neighbours.append((row + 1, col)) 

            # left
            if col - 1 >= 0 and grid[row][col - 1] == val and (row, col - 1) != parent:
                neighbours.append((row, col - 1))  

            # right
            if col + 1 <= C and grid[row][col + 1] == val and (row, col + 1) != parent:
                neighbours.append((row, col + 1))  

            return neighbours

        def dfs(row, col, parent: tuple, visited: set):
            
            # base case
            if (row, col) in visited:
                return True

            visited.add((row, col))

            for r, c in get_neighbours(row, col, parent, grid[row][col]):
                if not parent or parent != (r, c):
                    if dfs(row=r, col=c, parent=(row,col), visited=visited):   #* parent is row, col
                        return True

            return False
            
        visited = set()

        for row in range(R):
            for col in range(C):
                if (row,col) not in visited:
                    if dfs(row, col, None, visited):
                        return True
                
        return False
    
s = Solution()
print(s.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]))