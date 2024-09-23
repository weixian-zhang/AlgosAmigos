from typing import List

import heapq
class Solution:

    # time limit exceeded
    # O(n + k * nlogn) 
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = set([x for x in range(len(capital))])

        def reheapify():
            nonlocal projects

            projCapProfit = []

            for idx in projects:
                projCapProfit.append((profits[idx], capital[idx], idx))

            heapq._heapify_max(projCapProfit)

            return projCapProfit
        
        projCapProfit = reheapify()
        
        while k != 0 and len(projCapProfit) > 0:

            profit, cap, project = heapq.heappop(projCapProfit)
            heapq._heapify_max(projCapProfit)

            if w >= cap:
                w += profit
                k -= 1
                projects.remove(project)
                projCapProfit = reheapify()

            continue

        return w
    

    # 2 heap pattern
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for _ in range(k):

            while minCapital and minCapital[0][0] <= w:

                _, p = heapq.heappop(minCapital)

                heapq.heappush(maxProfit, -p)
            
            if not maxProfit:
                break

            w -= heapq.heappop(maxProfit)

        return w



s = Solution()

# print(s.findMaximizedCapital(1, 0, [1,2,3], [1,1,2]))
print(s.findMaximizedCapital(3, 0, [1,2,3], [0,1,2]))
# print(s.findMaximizedCapital(2, 0, [1,2,3], [0,1,1]))

