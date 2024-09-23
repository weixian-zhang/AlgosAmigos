# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # similar solution but more elegant with popping preorder instead of slicing
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        
        def build_tree_recurse(preorder: list[int], inorder: list[int]) -> TreeNode:

            if not preorder or not inorder:
                return None
            
            rootNum = preorder.pop(0)

            root = TreeNode(rootNum)

            midRootIdx = inorder.index(rootNum)

            root.left = build_tree_recurse(preorder, inorder[:midRootIdx])

            root.right = build_tree_recurse(preorder, inorder[midRootIdx + 1:])

            return root
        
        tree = build_tree_recurse(preorder, inorder)
        return tree
    
    # neetcode solution
    # def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        
    #     def build_tree_recurse(preorder: list[int], inorder: list[int]) -> TreeNode:

    #         if not preorder or not inorder:
    #             return None
            
    #         root = TreeNode(preorder[0])

    #         midRootIdx = inorder.index(preorder[0])

    #         root.left = build_tree_recurse(preorder[1:midRootIdx + 1], inorder[:midRootIdx])

    #         root.right = build_tree_recurse(preorder[midRootIdx + 1:], inorder[midRootIdx + 1:])

    #         return root
        
    #     tree = build_tree_recurse(preorder, inorder)
    #     return tree
        

s = Solution()
tn = s.buildTree([3,9,20,15,7], [9,3,15,20,7])