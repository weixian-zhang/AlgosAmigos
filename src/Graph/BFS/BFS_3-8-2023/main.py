

def bfs(graph, start_node):
    
    if len(graph) == 0:
        return []
    
    queue = []
    visited = []
    
    visited.append(start_node)
    queue.append(start_node)
    
    while len(queue) > 0:
        
        node = queue.pop(0)
        
        
        
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
                
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
    
    path = bfs(graph, 0)
    
    print(path)