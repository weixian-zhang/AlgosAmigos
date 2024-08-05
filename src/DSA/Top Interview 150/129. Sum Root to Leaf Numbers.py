# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my solution WOOT!
# Runtime: 34 ms, faster than 85.37% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 16.3 MB, less than 53.48% of Python3 online submissions for Sum Root to Leaf Numbers.
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        sums = 0
        num = ''

        def _dfs(root: TreeNode) -> TreeNode:
            nonlocal num, sums

            if not root:
                return ''
            
            num += str(root.val)

            if not root.left and not root.right:
                sums += int(num)

            if root.left:
                _dfs(root.left)
                num = num[:-1]

            if root.right:
                _dfs(root.right)
                num = num[:-1]

        _dfs(root)

        return sums


n9 = TreeNode(9, TreeNode(5), TreeNode(1))
n4 = TreeNode(4, n9,TreeNode(0))

s = Solution()
s.sumNumbers(n4)