# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # my solution - space O(n) with list
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        nodes = []

        def _preorder(root: TreeNode):
            if not root:
                return

            nodes.append(root)
            _preorder(root.left)
            _preorder(root.right)

        _preorder(root)

        for x in range(len(nodes) - 1):
            nodes[x].right = nodes[x + 1]
            nodes[x].left = None
            
    # most votes solution
    # Post-Order traversal to get to rightmost node and backtrack "upwards" tracking "previous" node
    # while setting each node to previous
    def flatten(self, root: TreeNode) -> None:

        prev: TreeNode = None

        def _post_order(root: TreeNode):
            nonlocal prev

            if not root:
                return None
            
            _post_order(root.right)

            _post_order(root.left)

            root.right = prev

            root.left = None

            prev = root

        _post_order(root)

    



n2 = TreeNode(2, TreeNode(3), TreeNode(4))
n5 = TreeNode(5, None, TreeNode(6))
n1 = TreeNode(1, n2, n5)

s = Solution()
s.flatten(n1)