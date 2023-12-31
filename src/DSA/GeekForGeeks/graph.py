
from collections import defaultdict
class Graph:

    def __init__(self) -> None:
        self.matrix = []
        self.nodeIdxMap = defaultdict(int)

    def dfs(self, g: dict):
        

        def _dfs(node: int, visited: list[int]):

            visited.append(node)

            print(node)

            for neighbour in g[node]:
                if neighbour not in visited:
                    _dfs(neighbour, visited)

        _dfs(list(g.keys())[0], [])

    
    def bfs(self, g: dict):
        from collections import defaultdict

        visited = []
        queue = []

        queue.append(list(g.keys())[0])

        while queue:

            node = queue.pop(0)
            visited.append(node)

            print(node)

            for neighbour in g[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    
    def add_node_adj_matrix(self, n):
        if not self.nodeIdxMap:
            self.nodeIdxMap[n] = 0
        elif n not in self.nodeIdxMap:
            lastKey = list(self.nodeIdxMap.keys())[-1]
            self.nodeIdxMap[n] = self.nodeIdxMap[lastKey] + 1

    def create_adjacency_matrix(self, n, edges: list[list]):


        matrix = [[0] * n for _ in range(n)]

        for i in range(len(edges)):
            src = self.nodeIdxMap[edges[i][0]]
            dest = self.nodeIdxMap[edges[i][1]]
            matrix[src][dest] = 1

        print(matrix)




g = {
    0: [1,2,3],
    1: [0],
    2: [0,3,4],
    3: [0,2],
    4: [2]
}
graph = Graph()
# graph.dfs(g)
# graph.bfs(g)

graph.add_node_adj_matrix(0)
graph.add_node_adj_matrix(1)
graph.add_node_adj_matrix(2)
graph.add_node_adj_matrix(4)
graph.add_node_adj_matrix(8)
graph.create_adjacency_matrix(5,[[0, 1], [1,4], [2,4],[2,8]])