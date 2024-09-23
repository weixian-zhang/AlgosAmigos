class Solution:
    
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        path = []
        leftBound, rightBound, = 0, len(matrix[0])
        topBound, bottomBound =  0, len(matrix)
        
        while leftBound < rightBound and topBound < bottomBound:
            
            # move right
            for toRight in range(leftBound, rightBound):
                path.append(matrix[topBound][toRight])
                
            topBound += 1
            
            # move down
            for row in range(topBound, bottomBound):
                path.append(matrix[row][rightBound-1])
                
            
            rightBound -= 1
            
            # for single row path or single column path
            if not (leftBound < rightBound and topBound < bottomBound):
                break
            
            # move left
            for toLeft in range(rightBound-1, leftBound - 1, -1):
                path.append(matrix[bottomBound - 1][toLeft])
                

            bottomBound -= 1
            
            # move up
            for up in range(bottomBound - 1, topBound - 1, -1):
                path.append(matrix[up][leftBound])
            
            
            leftBound += 1
            
            
        return path
        

        
    


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
        
        
        #[[23,18,20,26,25],[24,22,3,4,4],[15,22,2,24,29],[18,15,23,28,28]]))
        
        
        # [[1,2,3,4,5,6,7,8,9,10],
        # [11,12,13,14,15,16,17,18,19,20],
        # [21,22,23,24,25,26,27,28,29,30],
        # [31,32,33,34,35,36,37,38,39,40],
        # [41,42,43,44,45,46,47,48,49,50],
        # [51,52,53,54,55,56,57,58,59,60],
        # [61,62,63,64,65,66,67,68,69,70],
        # [71,72,73,74,75,76,77,78,79,80],
        # [81,82,83,84,85,86,87,88,89,90],
        # [91,92,93,94,95,96,97,98,99,100]]))
        
          #[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
          
          #[[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
          # #[[1,2,3],[4,5,6],[7,8,9]]))