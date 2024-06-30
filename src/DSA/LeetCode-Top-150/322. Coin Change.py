from functools import lru_cache
from typing import List

class Solution:

    # backtracking brute force - time exceeded
    def coinChange(self, coins: list[int], amount: int) -> int:
        
        min_coins = float('inf')

        dp = {} # { coin: amount }

        @lru_cache(None)
        def dfs(currCoins: int, currAmount: int):
            nonlocal min_coins

            if currAmount == 0:
                min_coins = min(min_coins, currCoins)
                dp[currAmount] = min_coins
                return 0
            if currAmount < 0:
                return -1
            
            if currAmount in dp:
                return dp[currAmount]
            
            for c in coins:
                dfs(currCoins + 1, currAmount - c)
            
            #return min_coins if min_coins != float('inf') else -1

        dfs(0, amount)

        return min_coins if min_coins != float('inf') else -1

    # model answer - DP top down
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(amount: int):

            if amount == 0:
                return 0
            
            if amount < 0:
                return -1
            
            min_coins = float('inf') # minimum coins needed, but accumulated from all sub-problems

            for coin in coins:
                result = dfs(amount - coin)
                if result != -1:
                    result += 1
                    min_coins = min(min_coins, result)

            # do a return after loop complete
            # also means after sub-problems complete where sub-problems branches out
            # for each item in loop
            # **this return goes to "result" variable
            return min_coins if min_coins != float('inf') else -1

        return dfs(amount)

        
    # botom up
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:

                # if non negative
                if c <= a:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float('inf') else -1



s = Solution()
#print(s.coinChange([186,419,83,408], 6249))
# print(s.coinChange([2,5,10,1], 27))
# print(s.coinChange([1], 0))
print(s.coinChange([1,2,5], 11))
#print(s.coinChange([2,5], 3))
# print(s.coinChange([1,2,5], 4))
# print(s.coinChange([1,2,5], 3))