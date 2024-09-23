# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def _inorder(node: TreeNode, nodeList: list[int]):
            if not node:
                return
            
            _inorder(node.left, nodeList)
            nodeList.append(node.val)
            _inorder(node.right,nodeList)
        
        nodeList = []
        _inorder(root, nodeList)

        N = len(nodeList)
        for x in range(N - 1):
            if nodeList[x] >= nodeList[x + 1]:
                return False
            
        return True


n1 = TreeNode(1)
n4 = TreeNode(4, TreeNode(3), TreeNode(6))
n5 = TreeNode(5, n1, n4)

s = Solution()
print(s.isValidBST(n5))