from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# solve using mobile on train :)
# Runtime: 24 ms, faster than 99.53% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 17.7 MB, less than 15.59% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
      
      if not root:
        return []
      
      l2r = False
      result = [[root.val]]
      queue = deque([root] if root else [])
     
      while queue:
        
        temp =[]
        
        for _ in range(len(queue)):
          
          n = queue.popleft()
          if n.left:
            temp.append(n.left)
          if n.right:
            temp.append(n.right)

        for n in temp:
          queue.append(n)
        
        if not temp:
           continue
        
        tv = [x.val for x in temp]
        tv = list(reversed(tv)) if not l2r else tv
        result.append(tv)

        if not l2r:
            l2r = True
        else:
            l2r = False
           
      return result 


n20 = TreeNode(20, TreeNode(15), TreeNode(7))
n3 = TreeNode(3, TreeNode(9), n20)

s = Solution()
print(s.zigzagLevelOrder(n3))