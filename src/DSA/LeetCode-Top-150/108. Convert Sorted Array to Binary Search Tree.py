# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        
        
        def _recurse(nums):
            
            # base case
            if len(nums) == 1:
                return  TreeNode(nums[0])
            if len(nums) == 0:
                return None
        
            mid = len(nums) // 2
            
            root = TreeNode(nums[mid])
            
            left = _recurse(nums[:mid])
            
            right =_recurse(nums[mid+1:])
            
            self.bst_insert(root, left)
            
            self.bst_insert(root, right)
                
            return root
        
        
        root = _recurse(nums)
        
        return root
        
        
    def bst_insert(self, root, node: TreeNode):
        
        if node is None:
            return 
        
        if node.val <= root.val:
            
            if root.left is None:
                root.left = node
            else:
                self.bst_insert(root.left, node)
                
        elif node.val >= root.val:
            
            if root.right is None:
                root.right = node
            else:
                self.bst_insert(root.right, node)
                
        
    
    def print_bst(self, node):
        queue = []
        
        queue.append(node)
        
        while len(queue) > 0:
            
            item = queue.pop(0)
            
            print(item.val)
            
            if item.left is not None:
                queue.append(item.left)
                
            if item.right is not None:    
                queue.append(item.right)
                
            
            
    
    
if __name__ == '__main__':
    s = Solution()
    root = s.sortedArrayToBST([0,1,2,3,4,5])#[-10,-3,0,5,9])
    
    s.print_bst(root)
        