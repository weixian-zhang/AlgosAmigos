
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import defaultdict
from typing import Optional
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        pass


d = {}
n1 = Node(1)
n3 = Node(3)

d[n1] = Node(11)
d[n3] = Node(33)

print(d[n3].val)