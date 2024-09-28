from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, depth):
            if not node:
                return depth

            left_tree = dfs(node.left, depth + 1)

            right_tree = dfs(node.right, depth + 1)

            return max(left_tree, right_tree)

        return dfs(root, 0)
        