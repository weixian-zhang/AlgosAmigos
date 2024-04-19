from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # help from neetcode and AlgosWithMichael
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = -float('inf')

        def dfs(node: TreeNode):
            nonlocal maxSum

            if not node:
                return 0
            
            
            leftSum = dfs(node.left)

            rightSum = dfs(node.right)

            # set 0 if left or right tree is negative, which means only current node.val is considered
            leftSum = max(leftSum, 0)
            rightSum = max(rightSum, 0)

            # compute max path sum with split path. A node with 2 children is considered a path, hence,
            # reason why adding left, right and current node
            maxSum = max(maxSum, leftSum + rightSum + node.val) 

            # but for return, conly "single path" and not including sum of split, which is not considered a path
            # in parent node.
            return node.val + max(leftSum, rightSum)

        dfs(root)

        return maxSum

        


n20 = TreeNode(20, TreeNode(15), TreeNode(7))
minus10 = TreeNode(-10, TreeNode(9), n20)

minus2 = TreeNode(-2, TreeNode(1), TreeNode(3))
minus3 = TreeNode(-3, None, TreeNode(-1))
n1 = TreeNode(1, TreeNode(2), TreeNode(3))

s = Solution()
#print(s.maxPathSum(n1))
print(s.maxPathSum(minus10))