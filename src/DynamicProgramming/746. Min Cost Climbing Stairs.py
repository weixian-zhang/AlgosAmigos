from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        N = len(cost)
        dp = [0] * N
        
        dp[-1] = cost[-1]
        dp[-2] = min(cost[-2])
                    
        for x in range(N - 2, -1, -1):
            dp[x] = min(cost[x] + dp[x - 2], dp[x-1])
                    
        return dp[-1]
        