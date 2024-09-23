
class Solution:
    

    def find_shortest_path(self, graph: dict, src: str, dest: str):
        from queue import PriorityQueue

        pq = PriorityQueue()
        visited = { k: False for k, v in graph.items() }
        costTracker = { k: [10**10, ''] for k, v in graph.items() }

        costTracker[src] = (0, src)
        
        pq.put((1, src))

        while pq.queue:

            currNode = pq.get()[1]

            visited[currNode] = True
                    
            for n, dist in graph[currNode]:


                if ( costTracker[currNode][0] + dist) < costTracker[n][0]:
                    costTracker[n][0] = costTracker[currNode][0] + dist
                    costTracker[n][1] = currNode

                if not visited[n]:
                    pq.put((dist, n))

    
        route = self.get_shortest_route(costTracker, src, dest)
        return route

    
    def get_shortest_route(self, costTracker: dict, src:str, dest: str) -> str:

        route = [dest]
        node = dest
        while node != src:
            dist, parent = costTracker[node]
            node = parent
            route.append(parent)

        return ' -> '.join(route[::-1])
            
            



graph = {
    'a': [['b',4], ['c',4]],
    'b': [['a',4], ['c',2]],
    'c': [['a',4], ['b',2], ['d',3],['e',1],['f',6]],
    'd': [['c',3], ['f',2]],
    'e': [['c',1], ['f',3]],
    'f': [['d',2], ['c',6], ['e',3]],
}


s = Solution()
print(s.find_shortest_path(graph, 'a', 'f'))