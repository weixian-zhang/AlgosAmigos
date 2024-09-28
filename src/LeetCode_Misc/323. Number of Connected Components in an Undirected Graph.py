from typing import Optional, List

# with path compression
# union by Rank
class UnionFind:

    def __init__(self) -> None:
        self.parent = []
        self.rank = []

    def make(self, n: list[int]):
        # index represents the n number, and element represents parent
        self.parent = [x for x in range(n)]
        self.rank = [1] * n # increase rank only if both sides have same rank

    def find(self, n: int):
        if self.parent[n] == n: # if parent[n] != n, continue to find parent node
            return self.parent[n]
        
        self.parent[n] = self.find(self.parent[n])   # path compression, collaspe parent for all child nodes
        return self.parent[n]

    def union(self, x, y):

        # ignore if both parent of x and y are the same

        # else perform union
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:

            # union y tree into x tree as x has more children nodes a.k.a rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1  # increase rank only if both sides have same rank
  


# use union find data structure that contains all unioned edges
# the number of 
class Solution:

    # union find - O(N Log N)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #edges = sorted(edges, key=lambda e: e[0])
        
        uf = UnionFind()
        uf.make(n)

        for n1, n2 in edges:
            uf.union(n1, n2)

        for x in range(n):  # run thru 1 more time for path compression
            uf.find(x)

        unq = set(uf.parent)

        return len(unq)
    
    # O(V + E)
    # build adjacency list, do DFS and track visited
    # number of DFS determines number of connected components
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        visited = set([])

        def dfs(v, graph):
            
            if v in visited:
                return 0
        

            visited.add(v)

            for neighbour in graph[v]:
                if neighbour not in visited:
                    dfs(neighbour, graph)

            return 1
            
        # build adjacency list
        graph = {k:[] for k in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        connected_components = 0
        for k, v in graph.items():
            if k not in visited:
                connected_components += dfs(k, graph)

        return connected_components 
    

s = Solution()

# print(s.countComponents(2, [[1,0]])) # 1
print(s.countComponents(5, [[0,1],[1,2],[3,4]])) # 2
print(s.countComponents(4, [[0,1],[2,3],[1,2]])) # 1
