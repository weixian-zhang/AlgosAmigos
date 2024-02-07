from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # neetcode solution
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            
            res.append(rightSide.val)
        
        return res
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def dfs(root: TreeNode, level: int, maxLevel):

            # Base Case
            if root is None:
                return
        
            # If this is the last node of its level
            if (maxLevel[0] < level):
                result.append(root.val)
                maxLevel[0] = level
        
            # Recur for right subtree first, then left subtree
            dfs(root.right, level+1, maxLevel)
            dfs(root.left, level+1, maxLevel)

        maxLevel = [0]
        dfs(root, 1, maxLevel)

        return result



    # my solution
    # Runtime: 43 ms, faster than 27.70% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 16.6 MB, less than 66.58% of Python3 online submissions for Binary Tree Right Side View.
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
    #     if not root:
    #         return []
        
    #     result = []
        
    #     def bfs(node, result: list[int]):
    #         from collections import deque

    #         queue = deque([node])

    #         while len(queue) > 0:

    #             tempView = []

    #             while len(queue) > 0:

    #                 n = queue.pop()
    #                 tempView.append(n)

    #             result.append(tempView[-1].val)

    #             for n in tempView:
    #                 if n.left:
    #                     queue.appendleft(n.left)

    #                 if n.right:
    #                     queue.appendleft(n.right)


    #     bfs(root, result)

    #     return result


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