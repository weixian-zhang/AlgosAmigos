# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        
        result, queue, childrenNodes = [],  [], []
        
        queue.append(root)

        while queue:

            sums = []
            count = 0

            while queue:
                
                count += 1
                n = queue.pop(-1)
                sums.append(n.val)

                if n.left:
                    childrenNodes.append(n.left)
                if n.right:
                    childrenNodes.append(n.right)

            while childrenNodes:
                queue.append(childrenNodes.pop(-1))
            
            result.append(sum(sums) / count)

        return result




# n20 = TreeNode(20, TreeNode(15), TreeNode(7))
# r = TreeNode(3, TreeNode(9), n20)

n1 = TreeNode(1, TreeNode(0), TreeNode(2))
n5 = TreeNode(5, TreeNode(4), TreeNode(6))
r = TreeNode(3, n1, n5)

s = Solution()
print(s.averageOfLevels(r))