from typing import List

class Solution:

    
    # attempt with cycle detection, unsuccessful
    def longestCycle(self, edges: List[int]) -> int:

        maxCycle = -1

        def dfs(node, adjList, visited, pathVisited):
            nonlocal maxCycle

            visited[node] = True
            pathVisited[node] = True

            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    dfs(neighbour, adjList, visited, pathVisited)
                
                # is visited but is node in same "visiting path"
                elif pathVisited[neighbour] == True:
                    maxCycle = max(maxCycle, len([x for x in pathVisited if x == True]) - 1)

            pathVisited[node] = False
        
        N = len(edges)
        visited = [False] * N
        pathVisited = [False] * N

        adjList = {n: [] for n in range(N)}
        for idx, e in enumerate(edges):
            if e != -1:
                adjList[idx].append(e)

        for n in range(len(edges)):
            if not visited[n]:
                dfs(n, adjList, visited, pathVisited)


        return maxCycle
    
    # use dict to track each node and the "steps" in DFS recursion of the path
    # Runtime: 869 ms, faster than 91.65% of Python3 online submissions for Longest Cycle in a Graph.
    # Memory Usage: 79 MB, less than 39.07% of Python3 online submissions for Longest Cycle in a Graph.
    def longestCycle(self, edges: List[int]) -> int:
        
        def dfs(currNode, currStep, visited, nodeToSteps):
            if visited[currNode] or currNode == -1:
                return -1
            
            if currNode in nodeToSteps and currStep > nodeToSteps[currNode]:
                return currStep - nodeToSteps[currNode]
        
            nodeToSteps[currNode] = currStep

            cycles = dfs(edges[currNode], currStep + 1, visited, nodeToSteps)

            visited[currNode] = True

            return cycles

        maxCycle = -1
        visited = [False] * len(edges)
        nodeToSteps = {}

        for src, _ in enumerate(edges):
            if not visited[src] and src != -1:
                cycles = dfs(src, 0, visited, nodeToSteps)
                maxCycle = max(maxCycle, cycles)

        return maxCycle
        

s = Solution()
# print(s.longestCycle([2,-1,3,1]))
s.longestCycle([3,3,4,2,3])