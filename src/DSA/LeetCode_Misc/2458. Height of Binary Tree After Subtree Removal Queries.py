# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# import collections
# class Solution:
#     def treeQueries(self, R: TreeNode, Q: list[int]) -> list[int]:
#         Depth, Height = collections.defaultdict(int), collections.defaultdict(int)

#         def dfs(node, depth):
#             if not node:
#                 return -1
#             Depth[node.val] = depth
#             cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
#             Height[node.val] = cur
#             return cur
#         dfs(R, 0)

#         cousins = collections.defaultdict(list) # Group nodes according to their depth. Keep the top 2 heights.
#         for val, depth in Depth.items():
#             cousins[depth].append((-Height[val], val))
#             cousins[depth].sort()
#             if len(cousins[depth]) > 2:
#                 cousins[depth].pop()

#         ans = []
#         for q in Q:
#             depth = Depth[q]
#             if len(cousins[depth]) == 1:  # No cousin, path length equals depth - 1.
#                 ans.append(depth - 1)
#             elif cousins[depth][0][1] == q:  # The removed node has the largest height, look for the node with 2nd largest height.
#                 ans.append(-cousins[depth][1][0] + depth)
#             else:   # Look for the node with the largest height.
#                 ans.append(-cousins[depth][0][0] + depth)
#         return ans
    
class Solution:
    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
        
        nodes = []
        depthTracker = {}
        heightTracker = {}
        
        
        def dfs(node: TreeNode, depth):
            nonlocal nodes, depthTracker, heightTracker

            if not node:
                return 0
            
            nodes.append(node.val)

            depthTracker[node.val] = depth

            leftHeight = dfs(node.left, depth + 1) + 1

            rightHeight = dfs(node.right, depth + 1) + 1

            currHeight = max(leftHeight, rightHeight)

            heightTracker[node.val] = currHeight 

            return currHeight

        dfs(root, 0)

        dhTracker =  {k: [] for k in depthTracker.values()}

        for nodeVal, depth in depthTracker.items():
            height = heightTracker[nodeVal]
            dhTracker[depth].append((height, nodeVal))
            dhTracker[depth].sort(reverse=True)
            while len(dhTracker[depth]) > 2:
                dhTracker[depth].pop()


        result = []
        for q in queries:
            depth = depthTracker[q]
            if len(dhTracker[depth]) == 1:  # No cousin, path length equals depth - 1.
                result.append(depth - 1)
            elif dhTracker[depth][0][1] == q:  # The removed node has the largest height, look for the node with 2nd largest height.
                result.append(dhTracker[depth][1][0] + depth)
            else:   # Look for the node with the largest height.
                result.append(dhTracker[depth][0][0] + depth)


        return result
                

# brute force - TLE
# class Solution:
#     def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:
#         import copy

#         cache = {}

#         heightOfTree = self.get_height(root)

#         allPossibleQueries =  (2 ** (heightOfTree + 1)) - 1 #self.get_all_nodes(root)
#         for q in range(1, allPossibleQueries + 1):
#             if q == root.val:
#                 continue
#             copiedRoot = copy.deepcopy(root)
#             height = self.delete_node(copiedRoot, q)
#             cache[q] = height

        
#         heights = []
#         for q in queries:
#             heights.append(cache[q])

#         return heights

#     def get_all_nodes(self, node: TreeNode):

#         def _preorder(node: TreeNode, result: list[int]):
#             if not node:
#                 return
            
#             result.append(node.val)
#             _preorder(node.left, result)
#             _preorder(node.right, result)

#         result = []
#         _preorder(node, result)
#         return result[1:]

#     def delete_node(self, node: TreeNode, target: int) -> int:
        
#         def _delete(parent: TreeNode, node: TreeNode):

#             if not node:
#                 return node
            
#             # find node 
#             if node.val == target:
#                 # delete node

#                 if parent.left == node:
#                     parent.left = None
#                 else:
#                     parent.right = None
#             else:
#                 _delete(node, node.left)
#                 _delete(node, node.right)

        
#         _delete(None, node)

#         height = self.get_height(node)

#         return height


#     def get_height(self, node: TreeNode):
        
#         def _preorder(node: TreeNode):

#             if not node:
#                 return 0
            
#             leftHeight = 1 + _preorder(node.left)

#             rightHeight = 1 + _preorder(node.right)

#             height = max(leftHeight,rightHeight)

#             return height
        
#         h = _preorder(node)
#         return h - 1


# n4 = TreeNode(4)
# n6 = TreeNode(6)
# n2 = TreeNode(2,n4,n6)
# n1 = TreeNode(1)
# n3 = TreeNode(3)
# n7 = TreeNode(7)
# n8 = TreeNode(8, n2, n1)
# n9 = TreeNode(9, n3,n7)
# n5 = TreeNode(5, n8,n9)

# n7 = TreeNode(7)
# n5 = TreeNode(5, None, n7)
# n6 = TreeNode(6)
# n4 = TreeNode(4, n6, n5)
# n2 = TreeNode(2)
# n3 = TreeNode(3, n2)
# n1 = TreeNode(1, n3,n4)

# n3 = TreeNode(3)
# n2 = TreeNode(2, None, n3)
# n1 = TreeNode(1, None, n2)
# n5 = TreeNode(5)
# n4 = TreeNode(4, n1, n5)

n4 = TreeNode(4)
n2 = TreeNode(2, n4)
n3 = TreeNode(3, None, n2)
n5 = TreeNode(5, n3)
n1 = TreeNode(1, None, n5)

s = Solution()
print(s.treeQueries(n1, [3,5,4,2,4]))
# print(s.treeQueries(n5, [3,2,4,8]))
# print(s.treeQueries(n4, [2,2,1,3,2]))