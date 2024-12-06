# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time and O(N) space
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        if not root:
            return True
        
        def _dfs(node):

            if not node:
                return 0

            left_height = 1 + _dfs(node.left)

            right_height = 1 + _dfs(node.right)

            if left_height > right_height and left_height - right_height > 1:
                return float('inf')

            if right_height > left_height and right_height - left_height > 1:
                return float('inf')

            return max(left_height, right_height)
        

        height = _dfs(root)

        if height == float('inf'):
            return False
        
        return True
    

n3 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

#n1 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))

n1 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
s = Solution()
s.isBalanced(n1)