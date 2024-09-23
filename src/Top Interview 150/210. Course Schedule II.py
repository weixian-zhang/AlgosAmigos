from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if numCourses == 1:
            return [0]
        
        hasCycle = False
        result = []
        visited = {x: False for x in range(numCourses)}
        adjList = {x: [] for x in range(numCourses)}
        recursionPath = {x: False for x in range(numCourses)}

        def hasCycleDFS(currNode) -> bool:
            nonlocal result, hasCycle

            if hasCycle:
                return
            
            visited[currNode] = True
            recursionPath[currNode] = True
            
            for nei in adjList[currNode]:
                if not visited[nei]:
                    hasCycle = hasCycleDFS(nei)
                    
                    # break upon cycle detected. If not its like ignoringcycle and continue
                    if hasCycle:
                        break
                    
                elif recursionPath[nei]:
                    hasCycle = True
                    break
            
            recursionPath[currNode] = False

            if currNode not in result and not hasCycle:
                result.append(currNode)

            return hasCycle

        
        for dest, src in prerequisites:
            adjList[src].append(dest)

        for src in list(adjList.keys()):
            has = hasCycleDFS(src)
            if has:
                return []
            
        return result[::-1]




s = Solution()
print(s.findOrder(3, [[1,0],[2,0],[0,1]]))
# print(s.findOrder(3, [[0,2],[1,2],[2,0]]))
# print(s.findOrder(2, [[0,1],[1,0]]))
# print(s.findOrder(2, [[1,0]]))
# print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))