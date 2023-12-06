from queue import PriorityQueue
import sys

class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], src: int) -> dict[int, int]:

        adjList = {}
        for x in range(n):
            adjList[x] = []

        for s, dest, weight in edges:
            adjList[s].append((dest, weight))

        dest = n - 1
        pq = PriorityQueue()
    
        visited = []
        # distant tracker with previous node tracking
        distTracker = {}
        for x in range(n):
            distTracker[x] = (sys.maxsize, None)

        distTracker[src] = (0, src)

        pq.put((0, src))

        while not pq.empty():

            currNode = pq.get()[1]
            visited.append(currNode)

            for dest, weight in adjList[currNode]:

                if dest in visited:
                    continue
                
                # calc shortest distant
                curr_weight = distTracker[currNode][0]
                if curr_weight + weight < distTracker[dest][0]:
                    distTracker[dest] = (curr_weight + weight, currNode)

                

                pq.put((curr_weight + weight, dest))


        result = {}
        for x in range(n):
            dist = distTracker[x][0]
            result[x] = dist if dist != sys.maxsize else -1

        # travese shortest path with previous node stored in distTracker
        src = 0
        dest = 3
        path = self.get_print_shortest_path(src, dest, distTracker)
        path = path[::-1]
        print(' -> '.join([str(x) for x in path]))

        return result
    
    def get_print_shortest_path(self,src, dest, distTracker: dict):
        
        
        prev = distTracker[dest][1]
        path = [dest, prev]

        while prev != src:
            prev = distTracker[prev][1]
            path.append(prev)

        return path

                

        

n = 5
edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
src = 0

# n=4
# edges=[[0,1,5],[0,2,7],[1,2,2],[1,3,6],[2,3,4]]
# src=1

s = Solution()
s.shortestPath(n, edges, src)
