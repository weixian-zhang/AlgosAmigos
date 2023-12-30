class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0 for x in range(n + 1)]
        dp[-2] = 1
        dp[-1] = 1


        for x in range(len(dp) - 3, -1,  -1):
            dp[x] = dp[x + 2] + dp[x + 1]

        return dp[0]




s = Solution()
print(s.climbStairs(2))
# print(s.climbStairs(3))
# print(s.climbStairs(6))
# print(s.climbStairs(11))