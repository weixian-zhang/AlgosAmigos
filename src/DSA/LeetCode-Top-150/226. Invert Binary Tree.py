# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        def _invert(node: TreeNode):
            if not node:
                return
            
            _invert(node.left)

            _invert(node.right)
            
            temp = node.left
            node.left = node.right
            node.right = temp

            
            
        _invert(root)
        return root

n2 = TreeNode(2, TreeNode(1), TreeNode(3))
n7 = TreeNode(7, TreeNode(6), TreeNode(9))
root = TreeNode(4, n2, n7)

s = Solution()
s.invertTree(root)
