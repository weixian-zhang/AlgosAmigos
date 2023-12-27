


def dfs(adj_graph, node_value, visited):
    
    if adj_graph == [] or len(adj_graph) == 0:
        return
    
    neighbours = adj_graph[node_value]
    
    if node_value in visited:
        return
    
    visited.append(node_value)
    
    for n in neighbours:
        dfs(adj_graph, n, visited)
        
    return visited
        

if __name__ == '__main__':
    
    graph = {
        0: tuple([1,2]),
        1: tuple([3,4]),
        2: tuple([]),
        3: tuple([1,5]),
        4: tuple([]),
        5: tuple([3,6,7,8]),
        6: tuple([5]),
        7: tuple([5,8]),
        8: tuple([5,7,9]),
        9: tuple([8])
    }
    
    path = dfs(graph, 0, [])
    
    print(path)
    
    
    