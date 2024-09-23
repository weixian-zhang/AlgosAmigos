class Solution:

    # use matrix to fill up zig zag shap
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        rows = numRows
        cols = len(s)
        diagonalCols = rows - 1

        matrix = [[] for x in range(rows)]
        for x in range(len(matrix)):
            matrix[x] = [0 for c in range(cols + 1)]

        w, i, j = 0, 0, 0

        while w <= len(s) - 1:

            if i <= rows - 1:
                matrix[i][j] = s[w]
                i += 1
                w += 1

            # reach end of row
            else:
                i -= 2
                for d in range(diagonalCols):

                    if w > len(s) - 1:
                        break
                    
                    j += 1
                    matrix[i][j] = s[w]
                    w += 1

                    if i > 0:
                        i -= 1
                    else:
                        i = 1
             

        result = []
        for r in range(rows):
            for c in range(len(matrix[0])):
                if matrix[r][c] != 0:
                    result.append(matrix[r][c])

        return ''.join(result)


s = Solution()
print(s.convert('ABCD', 3))
# print(s.convert('AB', 1))
# print(s.convert('PAYPALISHIRING', 3))
# print(s.convert('PAYPALISHIRING', 4))