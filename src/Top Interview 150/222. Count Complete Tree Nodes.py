# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        
        def _get_height_left(node: TreeNode ) -> (int,int):
            
            if not node:
                return 0

            return 1 + _get_height_left(node.left)
             

        
        def _get_height_right(node: TreeNode ) -> (int,int):
            
            if not node:
                return 0

            return 1 + _get_height_right(node.right)

            
        def _count_nodes(node: TreeNode):
            
            if not node:
                return 0
            
            leftHeight, rightHeight = _get_height_left(node), _get_height_right(node)
            
            if leftHeight == rightHeight:
                count = 2 ** leftHeight - 1
                return count
            else:
                leftCount = _count_nodes(node.left)
                rightCount = _count_nodes(node.right)
                count= 1 + leftCount + rightCount
                return count
            
        count = _count_nodes(root)
        return count
                
    
    
    
if __name__ == '__main__':
    
    # n1 = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n4 = TreeNode(4)
    # n5 = TreeNode(5)
    # n6 = TreeNode(6)
    
    # n1.left = n2
    # n1.right = n3
    # n2.left = n4
    # n2.right = n5
    # n3.left = n6
    
    # s = Solution()
    # s.countNodes(n1)
    
    # n1 = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n1.left = n2
    # n1.right = n3
    
    # s = Solution()
    # s.countNodes(n1)
    
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    
    s = Solution()
    s.countNodes(n1)

    