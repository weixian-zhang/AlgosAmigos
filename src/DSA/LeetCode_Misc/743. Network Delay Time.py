class Solution:
    
    # Dijkstra algorithm
    # Runtime: 691 ms, faster than 7.00% of Python3 online submissions for Network Delay Time.
    # Memory Usage: 20.4 MB, less than 5.58% of Python3 online submissions for Network Delay Time.
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        from queue import PriorityQueue
        
        graph = {k : [] for k in range(1, n + 1)}   # adjacency list

        for src, dest, weight in times:
            graph[src].append([dest, weight])
            #graph[dest].append([src, weight])

        pq = PriorityQueue()    
        visited = { k: False for k in range(1, n + 1) }
        costTracker = { k: 10**20 for k in range(1, n + 1) }

        costTracker[k] = 0
        pq.put((1, k))

        while pq.queue:

            currNode = pq.get()[1]

            visited[currNode] = True

            for neightbour, dist in graph[currNode]:

                if (costTracker[currNode] + dist) < costTracker[neightbour]:
                    costTracker[neightbour] = costTracker[currNode] + dist

                if not visited[neightbour]:
                    pq.put((dist, neightbour))

        result = max(list(costTracker.values()))
        return result if result != 10**20 else -1




s = Solution()
print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
print(s.networkDelayTime([[1,2,1]], 2, 1))