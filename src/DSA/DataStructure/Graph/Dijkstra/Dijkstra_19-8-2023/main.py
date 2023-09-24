
from queue import PriorityQueue
import sys

adj_list = {
    0: [(1, 4), (2,1)],
    1: [(0, 4), (2,2), (3, 1)], 
    2: [(0, 1), (1,2), (3, 5)],
    3: [(1, 1), (2,5), (4, 3)],
    4: [(3, 3)]
    }


def dijkstra_sp(graph: dict):
    
    dist = { x:sys.maxsize for x in graph.keys() }
    visited = []
    node_dist_tracker = {}
    pq = PriorityQueue()
    
    first_node = list(graph.keys())[0]
    pq.put((0, first_node))
    dist[first_node] = 0
    
    while len(pq.queue) > 0:   # going to "next selected" node
        
        curr_node = pq.get()
        curr_node_value = curr_node[1]
        curr_node_dist = curr_node[0]
        
        visited.append(curr_node_value)
        
        for node in graph[curr_node_value]: # looking every neighbours
            
            next_node = node[0]
            next_node_dist = node[1]
            
            if next_node in visited : continue   # if visited, skip
            
            new_dist_to_neighbour = dist[curr_node_value] + next_node_dist
            
            if new_dist_to_neighbour < dist[next_node]:
                dist[next_node] = new_dist_to_neighbour
                
            pq.put((next_node_dist, next_node))
            
    return dist
        
        
        
    
    

if __name__ == '__main__':
    dist = dijkstra_sp(adj_list)
    print(dist)