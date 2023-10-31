class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        columns = len(board[0]) - 1
        
        for i in range(len(board)):
            for j in range(columns):
                
                cell = board[i][j]
                liveCells = self._get_live_cells_of_8_neightbours(board, i, j)
                
                # live cell
                if cell == 1:
                    board[i][j] = self._live_cell_lesser_than_2(liveCells)
                    board[i][j] = self._live_cell_larger_equals_2_3(liveCells)
                    board[i][j] = self._live_cell_larger_3(liveCells)
                    
                # dead cell
                else:
                    board[i][j] = self._dead_cell_equals_3(liveCells)
    
    def _live_cell_lesser_than_2(self, cells: int) -> int:
        pass
    
    def _live_cell_larger_equals_2_3(self, cells: int) -> int:
        pass
    
    def _live_cell_larger_3(self, cells: int) -> int:
        pass
    
    def _dead_cell_equals_3(self, cells: int) -> int:
        pass
    
    # m = rows
    # n = cols
    def _get_live_cells_of_8_neightbours(board: list[list[int]], row: int, col: int):
        """returns total live cells of 8 neighbours
        """
        liveCells  = 0
        upperBound = 0
        lowerBound = len(board) - 1
        leftBound = 0
        rightBound = len(board[0]) - 1
        tlRow, tlCol = row, col
        
        # top left
        if row > 0:
            tlRow -= 1
        if col > 0:
            tlCol -= 1
        liveCells += board[tlRow][tlCol]
        
        # top
        tlRow, tlCol = row, col
        if row > 0:
            tlRow -= 1
        liveCells += board[tlRow][tlCol]
        
        # top right
        tlRow, tlCol = row, col
        if row > 0:
            tlRow -= 1
        if col < rightBound:
            tlCol += 1
        liveCells += board[tlRow][tlCol]
        
        # left
        tlRow, tlCol = row, col
        if col > 0:
            tlCol -= 1
        liveCells += board[tlRow][tlCol]
        
        # right
        tlRow, tlCol = row, col
        if col < rightBound:
            tlCol += 1
        liveCells += board[tlRow][tlCol]
        
        # bottom left
        tlRow, tlCol = row, col
        if row < lowerBound:
            tlRow += 1
        if col > 0:
            tlCol -= 1
        liveCells += board[tlRow][tlCol]
        
        # bottom
        tlRow, tlCol = row, col
        if row < lowerBound:
            tlRow += 1
        liveCells += board[tlRow][tlCol]
        
        # bottom right
        tlRow, tlCol = row, col
        if row < lowerBound:
            tlRow += 1
        if col < rightBound:
            tlCol += 1
        liveCells += board[tlRow][tlCol]
        
        return liveCells
    