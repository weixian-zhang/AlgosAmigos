
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import defaultdict
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        old_new = {}

        # do dfs on node
        def dfs(node):
            if node in old_new:
                return old_new[node]

            copy = Node(node.val)
            old_new[node] = copy

            for nei in node.neighbors:
               previously_copied = dfs(nei)
               copy.neighbors.append(previously_copied)

            return copy

        clone = dfs(node)
                    
        # return first item
        return clone if clone else None