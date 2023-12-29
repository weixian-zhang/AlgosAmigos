

class Graph:

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




g = {
    0: [1,2,3],
    1: [0],
    2: [0,3,4],
    3: [0,2],
    4: [2]
}
graph = Graph()
# graph.dfs(g)
graph.bfs(g)