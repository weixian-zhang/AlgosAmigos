# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        # breadth first search does not work
        # but preorder works
        # def _bfs(root):
            
        #     if root is None:
        #         return []
            
        #     result = []
        #     queue = []
            
        #     queue.append(root)
            
        #     while queue:
                
        #         node = queue.pop(0)
                
        #         result.append(node.val)
                
        #         if node.left is not None:
        #             queue.append(node.left)
                    
        #         if node.right is not None:
        #             queue.append(node.right)
                    
        #     return result
        
        def _preorder(node: TreeNode, result: list[int]):
            
            if node is None:
                result.append(None)
                return
            
            result.append(node.val)
            
            _preorder(node.left, result)
            
            _preorder(node.right, result)
            
            return result
                    
                    
        pResult = _preorder(p, [])
        qResult = _preorder(q, [])
        
        return pResult == qResult
        
            
    
    
    
if __name__ == '__main__':
    
    s = Solution()
    
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.right = TreeNode(4)
    
    s.isSameTree(p, q)