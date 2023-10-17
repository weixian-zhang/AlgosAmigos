class Solution:
    
    def numIslands(self, grid: list[list[str]]) -> int:
        
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        
        # using depth first search
        def dfs_1(grid, row, col):
            
            if row not in range(rows) or col not in range(cols):
                return
            if (row, col) in visited:
                return
            if grid[row][col] != '1':
                return
            
            directions = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
            
            visited.add((row, col))
            
            for dr, dc in directions:
                dfs_1(grid, dr, dc)
                
        def dfs_2(grid, row, col):
            
            if row not in range(rows) or col not in range(cols):
                return 0
            if (row, col) in visited:
                return 0
            if grid[row][col] != '1':
                return 0
            
            visited.add((row, col))
            
            dfs_2(grid, row-1, col)
            dfs_2(grid, row+1, col)
            dfs_2(grid, row, col-1)
            dfs_2(grid, row, col+1)
                
                    
        
        # using breadth first search
        def bfs(grid, row, col):
            
            queue = []
            
            visited.add((row,col))
            
            queue.append((row, col))
            
            while len(queue) > 0:
                
                row, col = queue.pop(0)
                
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                    (r, c) not in visited and
                    r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == '1'):
                        
                        queue.append((r,c))
                        visited.add((r, c))
                

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    #dfs_1(grid, r, c)
                    dfs_2(grid, r, c)
                    #bfs(grid, r, c)
                    islands += 1
                    
        return islands
                    
    

if __name__ == '__main__':
    
    # grid = [
    #         ["1","1","0","0","0"],
    #         ["1","1","0","0","0"],
    #         ["0","0","1","0","0"],
    #         ["0","0","0","1","1"]
    #         ]
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

    #grid = [["1"], ["1"]]
    
    #grid = [["1"]]
    
    #grid = [["1","0","1","1","0","1","1"]]
    
    s = Solution()
    
    print(s.numIslands(grid))
     
     