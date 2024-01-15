from typing import List
from collections import defaultdict

# detect cycle in directed graph
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True
        
        adjList = defaultdict(list)
        visited = defaultdict(bool)
        recursionPath = defaultdict(bool)

        def hasCycle(curr, visited: dict, recursionPath: list):
            
            has = False
            visited[curr] = True
            recursionPath[curr] = True

            for nei in adjList[curr]:

                if not visited[nei]:
                    has = hasCycle(nei, visited, recursionPath)
                    if has:
                        break
                    
                elif recursionPath[nei]:
                    has = True
                    break
                
            recursionPath[curr] = False
                
            return has


        for dest, src in prerequisites:
            adjList[src].append(dest)
        
        for src in adjList:
            visited[src] = False
            recursionPath[src] = False

        for node in list(adjList.keys()):
            has = hasCycle(node, visited, recursionPath)
            if has:
                return False

        return True
    

s = Solution()
print(s.canFinish(3, [[0,2],[1,2],[2,0]]))
# print(s.canFinish(2, [[1,0]]))
# print(s.canFinish(2, [[1,0],[0,1]]))
# print(s.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
