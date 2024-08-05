class Solution:
    
    # my solution with mirror/copied board
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        columns = len(board[0])

        mirrorBoard = [[] for x in range(len(board))]
        for x in range(len(mirrorBoard)):
            mirrorBoard[x] = [0 for x in range(columns)]
            
        for i in range(len(board)):
            for j in range(columns):
                
                cell = board[i][j]
                liveCells = self._get_live_cells_of_8_neightbours(board, i, j)
                
                # live cell
                if cell == 1:
                    if liveCells < 2:
                        cell = 0
                    elif liveCells >= 2 and liveCells <= 3:
                        cell = 1
                    elif liveCells > 3:
                        cell = 0
                    
                    mirrorBoard[i][j] = cell

                    
                # dead cell
                else:
                    if liveCells == 3:
                        mirrorBoard[i][j] = 1
                    
        
        for i in range(len(mirrorBoard)):
            for j in range(columns):
                board[i][j] = mirrorBoard[i][j]
                
    
    # m = rows
    # n = cols
    def _get_live_cells_of_8_neightbours(self, board: list[list[int]], row: int, col: int):
        """returns total live cells of 8 neighbours
        """
        liveCells  = 0
        upperBound = 0
        lowerBound = len(board) - 1
        leftBound = 0
        rightBound = len(board[0]) - 1
        
        # top left
        if not row - 1 < upperBound and not col - 1 < leftBound:
            liveCells += board[row - 1][col - 1]
        
        # top
        if not row - 1 < upperBound:
            liveCells += board[row - 1][col]
        
        # top right
        if not row - 1 < upperBound and not col + 1 > rightBound:
            liveCells += board[row - 1][col + 1]
        
        # left
        if not col - 1 < leftBound:
            liveCells += board[row][col - 1]
        
        # right
        if not col + 1 > rightBound:
            liveCells += board[row][col + 1]
        
        # bottom left
        if not row + 1 > lowerBound and not col - 1 < leftBound:
            liveCells += board[row + 1][col - 1]
        
        # bottom
        if not row + 1 > lowerBound:
            liveCells += board[row + 1][col]
        
        # bottom right
        if not row + 1 > lowerBound and not col + 1 > rightBound:
            liveCells += board[row + 1][col + 1]
        
        return liveCells
    
board = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
#[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

s = Solution()

s.gameOfLife(board)

print(board)
    