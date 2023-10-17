# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        
        # pre-order traversal node->left->right
        def _traverse(node: TreeNode) -> TreeNode:
            
            # base case
            if node is None:
                return 
            
            # swap
            tempLeft = node.left
            node.left = node.right
            node.right = tempLeft
            
            _traverse(node.left)
            
            _traverse(node.right)
            
            return node
            
        return _traverse(root)
    
    
    # breadth first search
    def display_inline(self, root: TreeNode):
        
        result = []
        queue = []
        
        queue.append(root)
        
        while len(queue) > 0:
            
            node = queue.pop(0)
            
            result.append(node.val)
            
            if node.left is not None:
                queue.append(node.left)
                
            if node.right is not None:
                queue.append(node.right)
                
        print(result)
    
    
    
if __name__ == '__main__':
    
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    n7 = TreeNode(7)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n6 = TreeNode(6)
    n9 = TreeNode(9)
    
    n4.left = n2
    n4.right = n7
    n2.left = n1
    n2.right = n3
    n7.left = n6
    n7.right = n9
    
    s = Solution()
    
    s.display_inline(n1)
    #s.display_inline(n4)
    
    result = s.invertTree(n1)
    
    s.display_inline(result)