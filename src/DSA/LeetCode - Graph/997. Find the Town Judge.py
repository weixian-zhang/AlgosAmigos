from typing import List

# find node without neighbours and node is a neighbour of every node
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adjList = {n: [] for n in range(1, n+1)}

        for src, dest in trust:
            adjList[src].append(dest)

        oneWithoutTrust = -1
        for k, v in adjList.items():
            if not v:
                oneWithoutTrust = k

        for k, v in adjList.items():
            if oneWithoutTrust not in v and k != oneWithoutTrust:
                return -1
        
        return oneWithoutTrust
    

s = Solution()
print(s.findJudge(2, [[1,2]]))  # 2
print(s.findJudge(3, [[1,3],[2,3]])) # 3
print(s.findJudge(3, [[1,3],[2,3],[3,1]])) # -1
print(s.findJudge(3, [[1,2],[2,3]])) 
