from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        result = []
        adjList = defaultdict(dict)

        # forward = multiple
        # backwards = divide
        def forward_or_backward(src: str, dest: str):
            if src < dest:
                return 'F'
            return 'B'
        
        def is_node_in_neighbours(node, neighbours: list[tuple]) -> float:
            for n in neighbours:
                if node in n:
                    return True, n[1]
            return False, -1

        def dfs(currNode: str, destNode: str, visited: list, accumuldatedProduct: int) -> int:
            
            result = -1.0

            if destNode in adjList[currNode]:
                result = accumuldatedProduct * adjList[currNode][destNode]
            else:

                # not direct neighbour, DFS
                for dest, val in adjList[currNode].items():
                    if dest in visited: continue

                    visited.append(currNode)

                    result = dfs(dest, destNode, visited, accumuldatedProduct * val)
                    
                    if result != -1.0:
                        break

            return result
                
            
        for (src, dest), val in zip(equations, values):
            adjList[src][dest] = val

            # backwards/reverse path e.g: b -> a
            adjList[dest][src] = 1 / val

            # for cases where destination is same as src, value is 1, result = 1/1
            adjList[src][src] = 1.0
            adjList[dest][dest] = 1.0


        for q in queries:

            qSrc = q[0]
            qDest = q[1]

            val = dfs(qSrc, qDest, [], 1)
            result.append(round(val, 5))

        return result
                    
                    

      




s = Solution()
print(s.calcEquation([["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]], 
                     [3.0,0.5,3.4,5.6], 
                     [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]  ))
# print(s.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))
# print(s.calcEquation([["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]))
# print(s.calcEquation([["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]))