# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    # neetcode solution
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # perform DFS on bot left and right tree at the same time
        def _dfs(left: TreeNode, right: TreeNode):
            if left is None and right is None:
                return True
            
            # tree not symmetrical as either side is None
            if left is None or right is None:
                return False
            
            return (
                    left.val == right.val and
                    _dfs(left.left, right.right) and
                    _dfs(left.right, right.left)
                )
            
        return _dfs(root.left, root.right)
             
            
    # my solution is faster and space efficient than offical solution
    # time: O(n + n + n) 
    # space: O(n-1 + n-1 + Height-of-tree)
    # def isSymmetric(self, root: TreeNode) -> bool:
    
    #     def _pre_order_traverse(root: TreeNode, view: list) -> TreeNode:
                
    #             if root is None:
    #                 view.append(None)
    #                 return view
                
    #             view.append(root.val)
                
    #             _pre_order_traverse(root.left, view)
                
    #             _pre_order_traverse(root.right, view)
                
                
    #             return view
            

    #     def _pre_order_traverse_get_mirror_view(root: TreeNode, mirrorView: list) -> TreeNode:
            
    #         if root is None:
    #             mirrorView.append(None)
    #             return mirrorView
            
    #         mirrorView.append(root.val)
                
            
    #         _pre_order_traverse_get_mirror_view(root.right, mirrorView)
            
    #         _pre_order_traverse_get_mirror_view(root.left, mirrorView)
            
    #         return mirrorView
            
            
    #     mirrorView = _pre_order_traverse_get_mirror_view(root.left, [])
        
    #     preOrderView = _pre_order_traverse(root.right, [])
        
    #     return mirrorView == preOrderView
            
            
            
            
if __name__ == '__main__':
    
    n1 = TreeNode(1)
    n2l = TreeNode(2)
    n2r = TreeNode(2)
    n3l = TreeNode(3)
    n3r = TreeNode(3)
    n4l = TreeNode(4)
    n4r = TreeNode(4)
    
    n1.left = n2l
    n1.right = n2r
    n2l.left = n3l
    n2l.right = n4l
    n2r.left = n4r
    n2r.right = n3r
    
    # n1 = TreeNode(1)
    # n2l = TreeNode(2)
    # n2r = TreeNode(2)
    # n3l = TreeNode(3)
    # n3r = TreeNode(3)
    # n4l = TreeNode(4)
    # n4r = TreeNode(4)
    
    # n1.left = n2l
    # n1.right = n2r
    # n2l.right = n3r
    # n2r.right = n3r
    
    
    s = Solution()
    print(s.isSymmetric(n1))
    