# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        def _inorder(node: TreeNode, nodeList: list[int]):
            
            if not node:
                return
            
            _inorder(node.left, nodeList)
            nodeList.append(node.val)
            _inorder(node.right, nodeList)
        
        nodeList = []
        _inorder(root, nodeList)

        r = nodeList[k-1]
        return r

n2 = TreeNode(2, TreeNode(1))
n6 = TreeNode(6)
n4 = TreeNode(4)
n3 = TreeNode(3, n2, n4)
n5 = TreeNode(5,n3, n6)

s = Solution()
print(s.kthSmallest(n5, 3))