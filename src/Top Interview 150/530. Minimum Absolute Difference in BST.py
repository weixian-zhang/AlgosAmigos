# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
import sys
class Solution:
    
    # in-order traversal, use a variable to store last value
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        
        midDiff = sys.maxsize
        lastVal = sys.maxsize
        
        def _dfs(node: TreeNode):
            
            nonlocal midDiff, lastVal
            
            if node is None:
                return
    
            _dfs(node.left)
            
            if lastVal == sys.maxsize:
                lastVal = node.val
            else:
                midDiff = min(midDiff, abs(lastVal - node.val))
                lastVal = node.val
            
            _dfs(node.right)
            
            
        _dfs(root)
        
        return midDiff
                
    
    # my solution, covert to Array, sort reverse and get min-diff for each num
    # def getMinimumDifference(self, root: TreeNode) -> int:
        
    #     minDiff = sys.maxsize
        
    #     treeAsList = []
        
    #     queue = []
    
    #     queue.append(root)
        
    #     while len(queue) > 0:
            
    #         n = queue.pop(0)
            
    #         treeAsList.append(n.val)
            
    #         if n.left is not None:
    #             queue.append(n.left)
                
    #         if n.right is not None:
    #             queue.append(n.right)
                
        
    #     treeAsList.sort(reverse=True)
        
    #     for x in range(len(treeAsList) - 1):
    #       minDiff=  min(minDiff, treeAsList[x] - treeAsList[x+1])
          
    #     return minDiff
        
# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:
        
#         minDiff = 10000
        
#         def _preorder(node: TreeNode):
#             nonlocal minDiff
            
#             # base case
#             if not node:
#                 return minDiff
            
#             if node.right is not None:
#                 minDiff = min(minDiff, node.right.val - node.val)
            
#             if node.left  is not None:
#                 minDiff = min(minDiff, node.val - node.left.val)
            
#             _preorder(node.left)
            
#             _preorder(node.right)
        
#         _preorder(root)
        
#         if root.left is not None:
#             largestFromLeft = self._get_largest_from_left(root.left)
#             minDiff = min(minDiff, root.val - largestFromLeft)
        
#         if root.right is not None:
#             smallestFromRight = self._get_smallest_from_right(root.right)
#             minDiff = min(minDiff, smallestFromRight - root.val)
        
#         return minDiff
    
#     def _get_largest_from_left(self, node: TreeNode):
        
#         if node.right is None:
#             return node.val
    
#         return self._get_largest_from_left(node.right)
        
    
#     def _get_smallest_from_right(self, node: TreeNode):
#         if node.left is None:
#             return node.val
        
#         return self._get_largest_from_left(node.left)

n1 = TreeNode(1)
n3 = TreeNode(3)
n2 = TreeNode(2)

n1.right = n3
n3.left = n2
s = Solution()
print(s.getMinimumDifference(n1)) 


n236 = TreeNode(236)
n104 = TreeNode(104)
n701 = TreeNode(701)
n227 = TreeNode(227)
n911 = TreeNode(911)

n236.left = n104
n236.right = n701
n104.right = n227
n701.right = n911

s = Solution()
print(s.getMinimumDifference(n236))

# n4 = TreeNode(4)
# n2 = TreeNode(2)
# n6 = TreeNode(6)
# n1 = TreeNode(1)
# n3 = TreeNode(3)

# n4.left = n2
# n4.right = n6
# n2.left = n1
# n2.right = n3

# s = Solution()
# print(s.getMinimumDifference(n4))

# n1 = TreeNode(1)
# n0 = TreeNode(0)
# n48 = TreeNode(48)
# n12 = TreeNode(12)
# n49 = TreeNode(49)

# n1.left = n0
# n1.right = n48
# n48.left = n12
# n48.right = n49

# s = Solution()
# print(s.getMinimumDifference(n1))