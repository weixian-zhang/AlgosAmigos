# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def __init__(self) -> None:
        self.root = None

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def _delete(parent: TreeNode, node: TreeNode, key):
            
            if not node:
                return
            
            if key > node.val:
                _delete(node, node.right, key)
            elif key < node.val:
                _delete(node, node.left, key)
            else:
                # found the node to delete
                # node have either no children or one child
                if not node.left:
                    if parent:
                        if parent.left == node:
                            parent.left = node.right
                        else:
                            parent.right = node.right
                    else:
                        self.root = node.right

                elif not node.right:
                    if parent:
                        if parent.left == node:
                            parent.left = node.left
                        else:
                            parent.right = node.left
                    else:
                        self.root =  node.left

                else:
                    
                    minKeyOnRight = node.right
                    while minKeyOnRight.left:
                        minKeyOnRight = minKeyOnRight.left

                    node.val = minKeyOnRight.val
                    _delete(node, node.right, node.val)
                # node has both left and right child

        self.root = root
        _delete(None, self.root, key)
        return self.root

    def print(self, node: TreeNode):

        if not node:
            return
        
        print(node.val)
        self.print(node.left)
        self.print(node.right)

# n7 = TreeNode(7)
# n4 = TreeNode(4)
# n2 = TreeNode(2)
# n3 = TreeNode(3)
# n6 = TreeNode(6)
# n5 = TreeNode(5)
# n5.left = n3
# n5.right = n6
# n3.left = n2
# n3.right = n4
# n6.right = n7
        
n1 = TreeNode(1)
n1.right = TreeNode(2)

s = Solution()
s.deleteNode(n1, 1)
        