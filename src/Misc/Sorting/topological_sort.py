

def topological_sort(dag: dict):

    if not dag:
        return []
    
    result = []
    stack = []
    visited = set()

    def dfs(node: str):
        
        visited.add(node)

        for n in dag[node]:
            if n not in visited:
                dfs(n)

        stack.append(node)


    for n in dag.keys():
        if n not in visited:
            dfs(n)

    while stack:
        result.append(stack.pop())

    return result


dag = {
    'g': ['b', 'f'],
    'b': ['c', 'f'],
    'f': ['d', 'e'],
    'a': ['b', 'c'],
    'c': ['d'],
    'd': [],
    'e': []
}

print(topological_sort(dag))