class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def hasPath(root: TreeNode, arr, x):
     
    # if root is None there is no path 
    if (not root):
        return False
     
    # push the node's value in 'arr' 
    arr.append(root.data)     
     
    # if it is the required node 
    # return true 
    if (root.data == x):     
        return True
     
    # else check whether the required node 
    # lies in the left subtree or right 
    # subtree of the current node 
    if (hasPath(root.left, arr, x) or
        hasPath(root.right, arr, x)): 
        return True
     
    # required node does not lie either in 
    # the left or right subtree of the current 
    # node. Thus, remove current node's value  
    # from 'arr'and then return false     
    arr.pop(-1) 
    return False


n6 = TreeNode(6, TreeNode(7, TreeNode(9), TreeNode(10)), TreeNode(8, TreeNode(11, TreeNode(13), TreeNode(14, TreeNode(15))), TreeNode(12)))

paths = []
hasPath(n6, paths, 15)

print('->'.join(str(x) for x in paths))