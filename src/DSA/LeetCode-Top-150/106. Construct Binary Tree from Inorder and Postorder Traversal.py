# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        
        def build_tree_recurse(inorder: list[int], postorder: list[int]):
            
            if not inorder or not postorder:
                return None
            
            rootNum = postorder.pop(-1)
            root = TreeNode(rootNum)
            midIdx = inorder.index(rootNum)

            root.right = build_tree_recurse(inorder[midIdx + 1:], postorder[midIdx:])

            root.left = build_tree_recurse(inorder[:midIdx], postorder[:midIdx])

            return root

        tree = build_tree_recurse(inorder, postorder)
        return tree


s = Solution()
s.buildTree([9,3,15,20,7], [9,15,7,20,3])
                                                                                                                                        