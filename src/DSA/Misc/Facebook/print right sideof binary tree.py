from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        result = []
        
        def bfs(node, result: list[int]):
            from collections import deque

            queue = deque([node])

            while len(queue) > 0:

                tempView = []

                while len(queue) > 0:

                    n = queue.pop()
                    tempView.append(n)

                result.append(tempView[-1].val)

                for n in tempView:
                    if n.left:
                        queue.appendleft(n.left)

                    if n.right:
                        queue.appendleft(n.right)


        bfs(root, result)

        return result


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n6.right = n8

s = Solution()
print(s.rightSideView(n1))