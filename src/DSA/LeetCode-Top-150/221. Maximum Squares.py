from typing import List

class Solution:

    # neetcode solution - recursion + memoization
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        R = len(matrix)
        C = len(matrix[0])
        cache = {}

        def dfs(i, j):

            if (i, j) in cache:
                return cache[(i, j)]
            
            # base case: 0 or out of bounds
            if i >= R or j >= C:
                return 0
            
            curr = int(matrix[i][j]) 

            # check top, right, down are all 1s
            right = dfs(i, j + 1)
            downRight = dfs(i + 1, j + 1)
            down = dfs(i + 1, j)

            cache[(i, j)] = 0

            if curr == 1:
                cache[(i, j)] = 1 + min(right, downRight, down)
            
            return cache[(i, j)]
        
        dfs(0, 0)

        r = max(cache.values())

        return r ** 2
    
    # own attemp of DP
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
        
    #     R = len(matrix) - 1
    #     C = len(matrix[0]) - 1

    #     dp = [0 * len(matrix[0]) for x in range(len(matrix))]

    #     dp[-1][-1] = 1 if dp[-1][-1] == '1' else 0

    #     for i in range(R, -1, -1):
    #         for j in range(C, -1, -1):

    #             if matrix[i][j] == int(0):
    #                 matrix[i][j] = 0
    #                 continue

    #             dp[i][j] = 1

    #             if (i + 1 <= R and j + 1 <= C and 
    #                 (matrix[i][j + 1] == int(1) and
    #                  matrix[i + 1][j] == int(1) and
    #                  matrix[i + 1][j + 1] == int(1)
    #                  )):




    

s = Solution()

#print(s.maximalSquare([["1","1","1"],["1","1","1"],["1","1","1"],["1","1","1"]]))
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# print(s.maximalSquare([["0","1"],["1","0"]]))
# print(s.maximalSquare(['0']))