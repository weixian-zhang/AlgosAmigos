
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


from typing import List

# Runtime: 96 ms, faster than 60.88% of Python3 online submissions for Construct Quad Tree.
# Memory Usage: 17.5 MB, less than 57.12% of Python3 online submissions for Construct Quad Tree.
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def all_same_values(rowStart: int, colStart: int, rowEnd: int, colEnd: int):
            
            visited = set()

            for i in range(rowStart, rowStart + rowEnd):
                for j in range(colStart, colStart + colEnd):
                    visited.add(grid[i][j])

                    if len(visited) > 1:
                        return False, 2

            return True, list(visited)[0]
                    

        def dfs(rowStart: int, colStart: int, rowEnd: int, colEnd: int) -> Node:

            same, val = all_same_values(rowStart, colStart, rowEnd, colEnd)

            if same:
                return Node(val, True, None, None, None, None)
            else:
                node = Node(0, False, None, None, None, None)
            

            node.topLeft = dfs(rowStart = rowStart, 
                                colStart= colStart , 
                                rowEnd=rowEnd // 2, 
                                colEnd=colEnd // 2)
            
            node.topRight = dfs(rowStart=rowStart, 
                                colStart= colStart + (colEnd // 2), 
                                rowEnd=rowEnd // 2, 
                                colEnd=colEnd // 2)
            
            node.bottomLeft = dfs(rowStart=rowStart + (rowEnd // 2), 
                                colStart= colStart, 
                                rowEnd=rowEnd // 2, 
                                colEnd=colEnd // 2)
            
            node.bottomRight = dfs(rowStart=rowStart + (rowEnd // 2), 
                                colStart= colStart + (colEnd // 2), 
                                rowEnd=rowEnd // 2, 
                                colEnd=colEnd // 2)

            return node
                   

        R = len(grid)
        C = R

        root = dfs(0, 0, R, C)

        return root
    

s= Solution()
# s.construct([[0,1],[1,0]])
s.construct([[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]])

