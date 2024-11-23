class Solution:

    # using recursion / DFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        upper = 0
        lower = len(image) - 1
        left = 0
        right = len(image[0]) - 1
        starting_color = image[sr][sc]
    
        def _traverse(row, col, visited):

            if row < upper or row > lower or col < left or col > right:
                return

            if (row, col) in visited:
                return
            
            if image[row][col] != starting_color:
                return

            
            image[row][col] = color

            visited.add((row, col))

            # up
            _traverse(row + 1, col, visited)

            # down
            _traverse(row - 1, col, visited)

            # left
            _traverse(row, col - 1, visited)

            # right
            _traverse(row, col + 1, visited)


        visited = set()

        _traverse(sr, sc, visited)

        return image