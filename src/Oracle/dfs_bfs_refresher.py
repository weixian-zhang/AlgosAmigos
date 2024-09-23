
def dfs_refresher(graph: dict):
    
    visited = set()
    result = []

    def dfs(curr: str):
        
        visited.add(curr)
        result.append(curr)
        for neighbour in graph[curr]:
            if neighbour not in visited:
                dfs(neighbour)

    curr = list(graph.keys())[0]
    return dfs(curr)



from collections import deque
def bfs_refresher(graph: dict):
    
    queue = deque([])
    visited = set()

    curr = list(graph.keys())[0]
    queue.append(curr)
    visited.add(curr)

    while queue:

        curr = queue.popleft()
        visited.add(curr)

        print(curr)

        for neighbour in graph[curr]:
            if neighbour not in visited:
                queue.append(neighbour)
    


graph = {
    '0': ['1'],
    '1': ['2', '3'],
    '2': [],
    '3': ['4'],
    '3': ['4'],
    '4': ['0']
}

# dfs_refresher(graph)

bfs_refresher(graph)

