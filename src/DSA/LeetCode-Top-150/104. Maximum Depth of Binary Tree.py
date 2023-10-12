# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    # 2 ways to write this recursion, "inline" and separate breakline
    
    # def maxDepth(self, root: TreeNode) -> int:
        
    #     def _traverse_tree(node: TreeNode, depth):
            
    #         # base case
    #         if node is None:
    #             return depth
    #         else:
    #             depth += 1
            
    #         leftDepth = _traverse_tree(node.left, depth)
            
    #         rightDepth = _traverse_tree(node.right, depth)
                
    #         return max(leftDepth, rightDepth)
            
    #     return _traverse_tree(root, 0)
    
    def maxDepth(self, root: TreeNode) -> int:
        
        def _traverse_tree(node: TreeNode, depth):
            
            # base case
            if node is None:
                return depth
            else:
                depth += 1
            
            return max(_traverse_tree(node.left, depth), _traverse_tree(node.right, depth))
            
        return _traverse_tree(root, 0)
        
        
    
    
    
if __name__ == '__main__':
    
    s = Solution()
    
    n3 = TreeNode(3)
    n3.left = TreeNode(9)
    n20 = TreeNode(20)
    n3.right = n20
    
    n20.left = TreeNode(15)
    n20.right = TreeNode(7)
    
    print(s.maxDepth(n3)) 