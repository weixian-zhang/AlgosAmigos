# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        def _dfs(node: TreeNode, sum: int):
           
           if node is None:
                return False
           
           sum -= node.val
        
           if not node.left and not node.right and sum == 0:
                return True
           
           leftHasSum = _dfs(node.left, sum)
           
           rightHasSum = _dfs(node.right, sum)
           
           return leftHasSum or rightHasSum

           
        hasSum =  _dfs(root, targetSum)
        return hasSum
     
     
     
if __name__ == '__main__':
    
    n5 = TreeNode(5)
    n4_1 = TreeNode(4)
    n4_2 = TreeNode(4)
    n8 = TreeNode(8)
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    
    n5.left = n4_1
    n5.right = n8
    n4_1.left = n11
    n11.left = n7
    n11.right = n2
    
    n8.left = n13
    n8.right = n4_2
    n4_2.right = n1
    
    s = Solution()
    s.hasPathSum(n5, 22)
    
    
    
    # n1 = TreeNode(-2)
    # n2 = TreeNode(-3)
    # n1.right = n2
    # s = Solution()
    # s.hasPathSum(n1, -5)
    