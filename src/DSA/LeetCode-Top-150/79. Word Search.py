from typing import List

# with the help of neetcode
# Runtime: 4372 ms, faster than 69.66% of Python3 online submissions for Word Search.
# Memory Usage: 17.3 MB, less than 44.66% of Python3 online submissions for Word Search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        R = len(board)
        C = len(board[0])

        wordIdx = 0
        words = list(word)

        def _dfs(row: int, col: int, wordIdx: int, visited: set):

            if wordIdx == len(words):
                return True

            if ((not row >= 0 or not row <= R-1 or not col >= 0 or not col <= C-1)
                or (board[row][col] !=  words[wordIdx]) or ((row,col) in visited)
                ):
                return False
            
            
            visited.add((row, col))

            
            if board[row][col] == words[wordIdx]:
                wordIdx += 1
                
            result = (
                        _dfs(row - 1, col, wordIdx, visited) or
                        _dfs(row + 1, col, wordIdx, visited) or
                        _dfs(row, col - 1, wordIdx, visited) or
                        _dfs(row, col + 1, wordIdx, visited)
                      )
            
            visited.remove((row, col))

            return result
            
            # if result: return True

            # # down
            # result = _dfs(row + 1, col, wordIdx, visited)
            # if result: return True

            # # left
            # result = _dfs(row, col - 1, wordIdx, visited)
            # if result: return True

            # # right
            # result = _dfs(row, col + 1, wordIdx, visited)
            # if result: return True

            
        for row in range(R):
            for col in range(C):
                if board[row][col] == words[wordIdx]:
                    result = _dfs(row, col, wordIdx, set())
                    if result:
                        return True

        return  False




s = Solution()
# print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
# "ABCB"))
print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],
"ABCESEEEFS"))
# # print(s.exist(["a"], "a"))
# # print(s.exist([["a","b"], ["c","d"]], "abcd"))
# # # print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
# print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))