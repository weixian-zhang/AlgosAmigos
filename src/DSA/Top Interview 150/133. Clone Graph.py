
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Runtime: 27 ms, faster than 99.71% of Python3 online submissions for Clone Graph.
# Memory Usage: 17.6 MB, less than 31.70% of Python3 online submissions for Clone Graph.
class Solution:
    def cloneGraph(self, node: Node) -> Node:

        if not node:
            return node
        
        def dfs(n: Node, visited, adjList: dict):
            
            if n.val in visited:
                return
            
            visited.append(n.val)

            if n.val not in adjList:
                adjList[n.val] = []
            
            for nei in n.neighbors:
                
                adjList[n.val].append(nei.val)

                dfs(nei, visited, adjList)

        
        adjList = {}

        dfs(node, [], adjList)

        nodeMap = {}

        for n in adjList.keys():
            nodeMap[n] = Node(n, [])

        for n, neighbours in adjList.items():
            for nei in neighbours:
                nodeMap[n].neighbors.append(nodeMap[nei])

        result = nodeMap[1]

        return result



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
# n1.neighbors = [n2,n4]
# n2.neighbors = [n1,n3]
# n3.neighbors = [n2,n4]
# n4.neighbors = [n1,n3]

s = Solution()
s.cloneGraph(n1)

