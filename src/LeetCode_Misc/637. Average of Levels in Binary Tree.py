# Definition for a binary tree node.
from typing import List, Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        queue = deque([root])
        result = []

        while len(queue) > 0:


            node_len = len(queue)
            node_sum = 0
            temp_nodes = []
            while queue:
                
                node = queue.popleft()
                node_sum += node.val

                if node.left:
                    temp_nodes.append(node.left)
                if node.right:
                    temp_nodes.append(node.right)

            result.append(node_sum / node_len)

            for n in temp_nodes:
                queue.append(n)

        return result
    
s = Solution()

n3 = TreeNode(3, TreeNode(9, TreeNode(15), TreeNode(7)), TreeNode(20))

print(s.averageOfLevels(n3))
                

            