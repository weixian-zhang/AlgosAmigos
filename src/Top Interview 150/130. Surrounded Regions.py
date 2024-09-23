from typing import List

# neetcode explanation
# Runtime: 124 ms, faster than 82.38% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 18.7 MB, less than 49.03% of Python3 online submissions for Surrounded Regions.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        firstRow = 0
        lastRow = len(board) - 1
        firstCol = 0
        lastCol = len(board[0]) - 1

        def is_edge(row: int, col: int) -> bool:
            if row == firstRow or row == lastRow or col == firstCol or col == lastCol:
                return True
            return False
        
        def is_oob(row, col):
            if row < firstRow or row > lastRow or col < firstCol or col > lastCol:
                return True
            return False
        
        def dfs(row: int, col: int) -> bool:

            if is_oob(row, col) or board[row][col] != 'O':
                return
            
            # if board[row][col] == 'X' or board[row][col] == 'U':
            #     return
            
            # if board[row][col] == 'O':
            #     board[row][col] = 'U'

            board[row][col] = 'U'

            # up
            dfs(row - 1, col)

            # down
            dfs(row + 1, col)

            # left
            dfs(row, col - 1)

            # right
            dfs(row, col + 1)
        
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if is_edge(row, col) and board[row][col] == 'O':
                    dfs(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'U':
                    board[row][col] = 'O'
                
        return board

s = Solution()

print(s.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))
print(s.solve([["O","O","O"],["O","O","O"],["O","O","O"]]))
print(s.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))