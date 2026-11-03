# 1 <= node len <= 10^4

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

# height of both left and right tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path_so_far = 0

        def dfs(node: TreeNode):
            nonlocal longest_path_so_far
            
            if not node:
                return 0

            left_path = dfs(node.left)

            right_path = dfs(node.right)
            # Longest path that bends at this node
            # 1
            #2 3
            longest_path_that_bends = left_path + right_path
            longest_path_so_far = max(longest_path_so_far, longest_path_that_bends)

            max_path_of_this_node_on_one_size = max(left_path, right_path)
            return  1 +  max_path_of_this_node_on_one_size


        dfs(root)
        return longest_path_so_far


s = Solution()
root = TreeNode(1, TreeNode(2))
r = s.diameterOfBinaryTree(root)
#r = s.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)))
print(r)


import unittest

class TestSolution(unittest.TestCase):

#    1
#   2 3
#  4
# 5
    def test_1(self):
        s = Solution()

        root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(4))), TreeNode(3))

        r = s.diameterOfBinaryTree(root)
        self.assertEqual(r, 4)


#    1
#   2 3
    def test_2(self):
        s = Solution()

        root = TreeNode(1, TreeNode(2), TreeNode(3))

        r = s.diameterOfBinaryTree(root)
        self.assertEqual(r, 2)


#    1
#   2
    def test_3(self):
        s = Solution()

        root = TreeNode(1, TreeNode(2))

        r = s.diameterOfBinaryTree(root)
        self.assertEqual(r, 1)