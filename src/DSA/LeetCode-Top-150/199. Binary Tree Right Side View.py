# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # reverse pre-order (NRL) with tracking of len of array correspond to height of tree
    # Runtime: 44 ms, faster than 26.68% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 16.3 MB, less than 20.83% of Python3 online submissions for Binary Tree Right Side View.
    def rightSideView(self, root: TreeNode) -> list[int]:
        
        def recurse(node: TreeNode, height: int, result: list[int]):
            
            if not node:
                return
            
            if height > len(result):
                result.append(node.val)

            # traverse right
            recurse(node.right, height + 1, result)

            # traverse left
            recurse(node.left, height + 1, result)
        
        result = []
        recurse(root, 1, result)

        return result

    # breadth first search
    # Runtime: 34 ms, faster than 89.41% of Python3 online submissions for Binary Tree Right Side View.
    # Memory Usage: 16.4 MB, less than 20.83% of Python3 online submissions for Binary Tree Right Side View.
    # def rightSideView(self, root: TreeNode) -> list[int]:

    #     if not root:
    #         return []
        
    #     result = []
    #     queue = []
    #     nextLevel = []

    #     queue.append(root)

    #     while queue:

    #         result.append(queue[-1].val)

    #         while queue:

    #             curr = queue.pop(0)

    #             if curr.left:
    #                 nextLevel.append(curr.left)

    #             if curr.right:
    #                 nextLevel.append(curr.right)


    #         while nextLevel:
    #             queue.append(nextLevel.pop(0))
    
    #     return result

        

s = Solution()

n2 = TreeNode(2, None, TreeNode(5))
n3 = TreeNode(3, None, TreeNode(4))
n1 = TreeNode(1, n2, n3)

s.rightSideView(n1)