from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # pre order traversal and swaps left and right at parent node
        def _preorder(node: TreeNode):

            if not node: # leaf node
                return None

            left = _preorder(node.left)

            right = _preorder(node.right)

            # parent node
            
            node.left = right

            node.right = left

            return node

        result =_preorder(root)

        return result        