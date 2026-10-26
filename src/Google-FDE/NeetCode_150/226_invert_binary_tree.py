
## 0 to 100 nodes

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:

        def inorder(node: TreeNode):

            if not node:
                return

            left = node.left
            right = node.right
            node.left = right
            node.right = left

            inorder(node.left)
            inorder(node.right)

        inorder(root)

        return root

s = Solution()
t4 = TreeNode(4, 
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(7, TreeNode(6), TreeNode(9)))

s.invertTree(t4)


import unittest

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution


  #    5
  #  3   4
  # 1 2 7 8
  #      9 10

  # none

  # 11

  # 11
  #   100


  #  55
  # 11