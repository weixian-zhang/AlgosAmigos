import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> list[TreeNode]:
        
        # root = self.init_tree()
        
        # if n == 3:
        #     return root
        
        result = []
        
        def _backtrack(n):
            
            if n == 0:
                return []
            if n == 1:
                return [TreeNode()]
            
            for l in range(n):
                
                r = n - 1 - l
                
                if l == 2:
                    pass
                
                leftTree = _backtrack(l)
                
                rightTree = _backtrack(r)
            
            if leftTree is None:
                pass
                
            for t1 in leftTree:
                for t2 in rightTree:
                    root = TreeNode(0)
                    root.left = t1
                    root.right = t2
                    result.append(root)
        
        # def _recurse(node, currentNodeNum, nodeLimit):
        #     nonlocal root
            
        #     # base
        #     if currentNodeNum >= nodeLimit:
        #         result.append(copy.deepcopy(root))
        #         return
            
            
        #     if not self.node_has_2_children(node) and (currentNodeNum + 2) <= nodeLimit:
        #         node.left = TreeNode(0)
        #         node.right = TreeNode(0)
        #         currentNodeNum += 2
            
            
        #     if len(result) != nodeLimit - 2:
        #         _recurse(node.left, currentNodeNum, nodeLimit)
                
        #         # backtrack left
        #         currentNodeNum  = 3
        #         root = self.init_tree()
                    
        #         _recurse(root.right, currentNodeNum, nodeLimit)
                
        #         # backtrack right
        #         currentNodeNum  = 3
        #         root = self.init_tree()
                
        #_recurse(root, 3, n)
        
        _backtrack(4)
        
        return result
        
    
    def node_has_2_children(self, node: TreeNode):
        if node.left is not None and node.right is not None:
            return True
        return False
    
    def init_tree(self):
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        return root





def list_to_binary_tree_recursion(nodes=[1,2,3,4,5,6,7]):
    
    if nodes == []:
        return
        
    root = TreeNode(1)
    
    def _recurse(idx, node):
        
        leftChildIdx = 2*idx + 1
        rightChildIdx = 2*idx + 2
        
        # base
        if idx == len(nodes) - 1 or leftChildIdx > len(nodes) - 1 or rightChildIdx > len(nodes) - 1:
            return
        
        if leftChildIdx <= len(nodes) - 1:
            node.left = TreeNode(nodes[leftChildIdx])
            _recurse(leftChildIdx, node.left)
            
        if rightChildIdx <= len(nodes) - 1:
            node.right = TreeNode(nodes[rightChildIdx])
            _recurse(rightChildIdx, node.right)
            
    
    _recurse(0, root)
    return root


def list_to_binary_tree_level_order_traversal(nodes=[1,2,3,4,5,6,7]):
    
    queue = []
    
    root = TreeNode(nodes[0])
    queue.append(root)
    idx = 1
    
    while len(queue) > 0:
        
        current_node = queue.pop(0)
        
        if idx <= len(nodes) - 1:
            current_node.left = TreeNode(nodes[idx])
            queue.append(current_node.left)
            idx += 1
            
        if idx <= len(nodes) - 1:
            current_node.right = TreeNode(nodes[idx])
            queue.append(current_node.right)
            idx += 1
            
    return root
        

def in_order_traversal(node: TreeNode):
    
    def _recurse(node):
        
        if node is None:
            return
        
        _recurse(node.left)
        
        print(node.val)
        
        _recurse(node.right)
        
    _recurse(node)


if __name__ == '__main__':
    # r1 = list_to_binary_tree_recursion()
    # in_order_traversal(r1)
    
    # r2 = list_to_binary_tree_level_order_traversal()
    # in_order_traversal(r2)
    
    s = Solution()
    r3 = s.allPossibleFBT(7)
    
    for bt in r3:
        in_order_traversal(bt)