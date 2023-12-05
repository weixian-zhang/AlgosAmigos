# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # breadth first search
    # Runtime: 34 ms, faster than 89.41% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 16.4 MB, less than 20.83% of Python3 online submissions for Binary Tree Right Side View.
    def rightSideView(self, root: TreeNode) -> list[int]:

        if not root:
            return []
        
        result = []
        queue = []
        nextLevel = []

        queue.append(root)

        while queue:

            result.append(queue[-1].val)

            while queue:

                curr = queue.pop(0)

                if curr.left:
                    nextLevel.append(curr.left)

                if curr.right:
                    nextLevel.append(curr.right)


            while nextLevel:
                queue.append(nextLevel.pop(0))
    
        return result

        

s = Solution()

n2 = TreeNode(2, None, TreeNode(5))
n3 = TreeNode(3, None, TreeNode(4))
n1 = TreeNode(1, n2, n3)

s.rightSideView(n1)