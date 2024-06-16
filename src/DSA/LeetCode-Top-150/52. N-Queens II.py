class Solution:
    def totalNQueens(self, n: int) -> int:
        
        colPrevQueen = set()
        positiveDiags= set()
        negativeDiags = set()
        queens = 0
        result = 0

        # recursive iterate row
        # "try" placing Q in column, backtrack by col
        def backtrack(row):
            nonlocal result

            # base case
            if row == n:
                result += 1
                return
            
            for col in range(n):

                posDiag = row + col
                negDiag = row - col

                if col in colPrevQueen or posDiag in positiveDiags or negDiag in negativeDiags:
                    continue
                
                
                colPrevQueen.add(col)
                positiveDiags.add(posDiag)
                negativeDiags.add(negDiag)

                backtrack(row + 1)

                # backtrack remove previously added data
                colPrevQueen.remove(col)
                positiveDiags.remove(posDiag)
                negativeDiags.remove(negDiag)

        
        backtrack(0)

        return result


s = Solution()

print(s.totalNQueens(4))









# understanding positive diagonal and negatve diagonal
matrix = [
    # 0   1   2   3
    [ 1,  2,  3,  4], # 0
    [ 5,  6,  7,  8], # 1
    [ 9, 10, 11, 12], # 2
    [13, 14, 15, 16]  # 3
]

from collections import defaultdict

def traverse_positive_diagonals(matrix):
    n = len(matrix)
    if n == 0:
        return []
    
    m = len(matrix[0])
    positiveDiagonal = defaultdict(list)
    
    negativeDiagonal = defaultdict(list)
    
    # Fill the diagonals dictionary
    for i in range(n):
        for j in range(m):
            positiveDiagonal[i + j].append(matrix[i][j])

    # Fill the positiveDiagonal dictionary
    for i in range(n):
        for j in range(m):
            negativeDiagonal[i - j].append(matrix[i][j])
    
    # Collect results in order of increasing sums of indices

    result = []
    for k in sorted(positiveDiagonal.keys()):
        result.append(positiveDiagonal[k])
    
    return result

# Example usage:
matrix = [
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
]

diagonals = traverse_positive_diagonals(matrix)
for diagonal in diagonals:
    print(diagonal)

