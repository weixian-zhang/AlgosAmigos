from typing import List

#Beats 100%
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        R = len(matrix)
        C = len(matrix[0])
        numIdxMap = {}
        result = []

        for i in range(R):
            row = matrix[i]
            minColIdx = row.index(min(matrix[i]))
            minValInRow = matrix[i][minColIdx]
            isLuckyNum = True
            
            for r in range(R):
                if r != i and matrix[r][minColIdx] > minValInRow:
                    isLuckyNum = False
                    break

            if isLuckyNum:
                result.append(minValInRow)

        return result
    

s = Solution()
print(s.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
print(s.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
print(s.luckyNumbers([[7,8],[1,2]]))

