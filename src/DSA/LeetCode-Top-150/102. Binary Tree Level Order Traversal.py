# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        
        if not root:
            return []
        
        result = [[root.val]]
        queue = []

        queue.append(root)

        while queue:

            temp = []

            while queue:
                
                
                node = queue.pop(0)

                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            if temp:
                result.append([x.val for x in temp])

            for n in temp:
                queue.append(n)


        return result
    

# n3 = TreeNode(3,
#               TreeNode(9), TreeNode(20, 
#                         TreeNode(15), TreeNode(7)))


n4  = TreeNode(4)
n5  = TreeNode(5)
n2 = TreeNode(2, n4)
n3  = TreeNode(3, n5)
n1 = TreeNode(1, n2, n3)

s = Solution()
print(s.levelOrder(n1))