class TreeNode:
    def __init__(self, val = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root: TreeNode) -> int:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left_total = dfs(node.left)
            right_total = dfs(node.right)
            total = 1 + max(left_total, right_total)

            return total

        return dfs(root)

    def _maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        def dfs(node: TreeNode, depth: int = 0) -> None:
            nonlocal max_depth

            # base case
            if not node:
                return None

            depth += 1

            max_depth = max(depth, max_depth)

            # recursive case
            dfs(node.left, depth)
            dfs(node.right, depth)


        dfs(root)
        return max_depth

s = Solution()
print(s.maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))