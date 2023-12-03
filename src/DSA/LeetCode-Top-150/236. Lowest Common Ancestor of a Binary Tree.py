# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# my initial solution - Time Limit Exceeded
# build 2 tables to track Left and Right trees descendant
# table is a dict where descendant_tracker[node number] = [descendant nodes]
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass

        if p == root:
            return p
        if q == root:
            return q
        
        # build a left tree descendant tracker
        leftDescTracker = {}
        ldt = self._build_descendant_tracker(root.left)
        reversedKeys = [k for k in ldt.keys()][::-1]
        for x in reversedKeys:
            leftDescTracker[x] = ldt[x]

        # build right tree descendant tracker
        rightDescTracker = {}
        rdt = self._build_descendant_tracker(root.right)
        reversedKeys = [k for k in rdt.keys()][::-1]
        for x in reversedKeys:
            rightDescTracker[x] = rdt[x]

        # check if p q in different trees
        if (p in leftDescTracker and q in rightDescTracker 
            or q in leftDescTracker and p in rightDescTracker):
            return root

        # p and q are in same tree
        if p in leftDescTracker and q in leftDescTracker:
            # from p, is q a descendant
            if q in leftDescTracker[p]:
                return p
            # from q, is p a descendant
            elif p in leftDescTracker[q]:
                return q
            # loop  each key node in desc tracker to find both descendants
            else:
                for k, _ in leftDescTracker.items():
                    if q in leftDescTracker[k] and p in leftDescTracker[k]:
                        return k
                    
        if p in rightDescTracker and q in rightDescTracker:
            if q in rightDescTracker[p]:
                return p
            elif p in rightDescTracker[q]:
                return q
            else:
                for k, _ in rightDescTracker.items():
                    if q in rightDescTracker[k] and p in rightDescTracker[k]:
                        return k
                
    def _build_descendant_tracker(self, node) -> dict:
        tracker = {}

        def bfs(node) -> list[TreeNode]:

            if not node:
                return []
            
            result = []
            queue =[]

            queue.append(node)

            while queue:

                n = queue.pop(0)

                result.append(n)

                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)

            return result

        def preorder(node):
            if not node:
                return
            
            leftDesc = bfs(node.left)
            rightDesc = bfs(node.right)
            tracker[node] = leftDesc + rightDesc

            if node.left:
                preorder(node.left)
            
            if node.right:
                preorder(node.right)

        preorder(node)

        return tracker
            


        

n7 = TreeNode(7)
n4 = TreeNode(4)
n2 = TreeNode(2)
n2.left = n7
n2.right = n4

n6 = TreeNode(6)
n5 = TreeNode(5)
n5.left = n6
n5.right = n2

n0 = TreeNode(0)
n8 = TreeNode(8)
n1 = TreeNode(1)
n1.left = n0
n1.right = n8

n3 = TreeNode(3)
n3.left = n5
n3.right = n1

s = Solution()
# s.lowestCommonAncestor(n3, n5, n1)
# s.lowestCommonAncestor(n3, n5, n4)

# n1 = TreeNode(1)
# n2 = TreeNode(2)
# n1.left = n2
# s.lowestCommonAncestor(n1, n1, n2)

nm1 = TreeNode(-1)
n0 = TreeNode(0)
n3 = TreeNode(3)
nm2 = TreeNode(-2)
n4 = TreeNode(4)
n8= TreeNode(8)
nm1.left = n0
nm1.right = n3
n0.left = nm2
n0.right = n4
n3.left = n8
s.lowestCommonAncestor(nm1, n8, n4)


