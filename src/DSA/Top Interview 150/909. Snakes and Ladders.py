from typing import List

class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque

        R = len(board)
        C = len(board[0])

        def square_num_to_rowcol_map() -> dict:
            from collections import defaultdict

            sbMap = defaultdict(tuple)

            rowIdx = R - 1
            squares = R*C
            for row in range(R):
                
                if rowIdx % 2 != 0:
                    for col in range(C):
                        sbMap[squares] = (row, col)
                        squares -= 1
                else:
                    for col in range(C-1, -1, -1):
                        sbMap[squares] = (row, col)
                        squares -= 1

                rowIdx -= 1

            return sbMap

        moves = 0
        queue = deque([(1, 0)])
        sbMap = square_num_to_rowcol_map()
        visited = set([1])

        while queue:

            currSquare, moves = queue.popleft()

            for x in range(1, 7):
                
                nextSquare = currSquare + x
                
                row, col = sbMap[nextSquare]

                
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                
                if nextSquare == R*C:
                    return moves + 1
                
                if nextSquare not in visited:
                    visited.add(nextSquare)
                    queue.append([nextSquare, moves + 1])

        return - 1


        

s = Solution()
print(s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [-1,35,-1,-1,13,-1],
                          [-1,-1,-1,-1,-1,-1],
                          [-1,15,-1,-1,-1,-1]]))

    # attempted DFS, failed terribly
    # def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
    #     R = len(board)
    #     C = len(board[0])
    #     squares = R*C
    #     result = squares
    #     visited = { x:False for x in range(1, squares + 1) }
    #     adjList = {x:[] for x in range(1, squares + 1)}
    #     snlBoard = [[c for c in board[row]] for row in range(len(board))]

    #     def col_in_bounds(col):
    #         if col >= 0 and col <= C - 1:
    #             return True
    #         return False
        
    #     # def dfs(currNode: int, moves: int, visited: dict):
    #     #     nonlocal result

    #     #     moves += 1
    #     #     visited[currNode] = True

    #     #     if currNode == R*C:
    #     #         result = min(result, moves)
    #     #         return
            
    #     #     for n in adjList[currNode]:
    #     #         if not visited[n]:
    #     #             dfs(n, moves, visited)
    #     #             moves -= 1

    #     def bfs(node: int):
    #         nonlocal result
    #         from collections import deque

    #         queue = deque([node])

    #         while queue:

    #             curr = queue.popleft()
    #             visited[curr] = True

    #             #if curr == R*C: # last cell of board
    #             result = min(result, R*C - curr)

    #             for nei in adjList[curr]:
    #                 if not visited[nei]:
    #                     queue.append(nei)

            

        
    #     # build actual snake and ladder board
        
    #     rowIdx = R - 1
    #     for row in range(R):
    #         for col in range(C):
    #             snlBoard[row][col] = squareNums

    #             squareNums -= 1

    #         # alternating order left 2 right, right 2 left
    #         if rowIdx % 2 == 0:
    #             snlBoard[row] = list(reversed(snlBoard[row]))

    #         rowIdx -= 1
        
    #     for row in range(R):
    #         for col in range(C):
    #             if board[row][col] == -1:
    #                 continue
    #             snlBoard[row][col] = (snlBoard[row][col], board[row][col])

        
    #     # build adjacency list
    #     rowIdx = R - 1
    #     for row in range(R-1, -1, -1):
    #         for col in range(C):
    #             cellVal = snlBoard[row][col]
    #             if row == 5:
    #                 pass
    #             if type(cellVal) == tuple:
    #                 node = cellVal[0]
    #                 nei1 = cellVal[1]
    #                 adjList[node].append(nei1)
    #                 cellVal = node

    #             for x in range(cellVal + 1, cellVal + 7):
    #                 if x <= R*C:
    #                     adjList[cellVal].append(x)

    #                 # if col_in_bounds(col - 1):
    #                 #     adjList[node].append(snlBoard[row][col - 1])
    #                 # if col_in_bounds(col + 1):
    #                 #     adjList[node].append(snlBoard[row][col + 1])
    #             # else:
    #             #     if col_in_bounds(col + 1):
    #             #             cellVal = snlBoard[row][col + 1]
    #             #             cellVal = cellVal if type(cellVal) != tuple else cellVal[0]
    #             #             adjList[snlBoard[row][col]].append(cellVal)
    #             #     if col_in_bounds(col - 1):
    #             #             cellVal = snlBoard[row][col - 1]
    #             #             cellVal = cellVal if type(cellVal) != tuple else cellVal[0]
    #             #             adjList[snlBoard[row][col]].append(cellVal)
    #                 #even row
    #                 # if rowIdx % 2 == 0:
    #                 #     if col_in_bounds(col + 1):
    #                 #         cellVal = snlBoard[row][col + 1]
    #                 #         cellVal = cellVal if type(cellVal) != tuple else cellVal[0]
    #                 #         adjList[snlBoard[row][col]].append(cellVal)
    #                 # else:
    #                 #     

    #         rowIdx -= 1

    #     bfs(list(adjList.keys())[0])

    #     return result
    

    