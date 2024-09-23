from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        nodes = set()

        for e in edges:
            nodes.update(set(e))

        adjList = {n : [] for n in nodes}

        for e in edges:
            src = e[0]
            dest = e[1]
            adjList[src].append(dest)
            adjList[dest].append(src)

        for k, v in adjList.items():
            if len(v) == len(nodes) - 1:
                return k


s = Solution()
s.findCenter([[1,2],[2,3],[4,2]])