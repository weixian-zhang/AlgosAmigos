from typing import List

class Solution:

    # using Matrix + DFS - memory limit exceeded
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        matrix = [[0] * n for x in range(n + 1)]

        for e in edges:
            src = e[0]
            dest = e[1]
            matrix[src][dest] = 1
            matrix[dest][src] = 1

        visited = {n: False for n in range(n + 1)}

        def dfs(node: int):

            visited[node] = True

            for nIdx in range(len(matrix[node])):
                if not visited[nIdx]  and matrix[node][nIdx] == 1:
                    dfs(nIdx)
                
            return False
        
        dfs(source)

        return visited[destination]
    

    # try using adjacency list + BFS - Success
    # Runtime: 3677 ms, faster than 5.00% of Python3 online submissions for Find if Path Exists in Graph.
    # Memory Usage: 116.6 MB, less than 47.51% of Python3 online submissions for Find if Path Exists in Graph.
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import deque

        adjList = {n: [] for n in range(n)}

        queue = deque([source])
        visited = {n: False for n in range(n)}

        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited[source] = True

        while queue:

            node = queue.popleft()
            if node == destination:
                return True
            
            visited[node] = True

            for neighbour in adjList[node]:
                if not visited[neighbour]:
                    queue.appendleft(neighbour)

        return False
    

s = Solution()
print(s.validPath(10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5))
# print(s.validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9))
# print(s.validPath(3, [[0,1],[1,2],[2,0]], 0 , 2))
# print(s.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0 , 5))