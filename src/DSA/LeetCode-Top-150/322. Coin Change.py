class Solution:

    # greedy algorithm - does not work
    # def coinChange(self, coins: list[int], amount: int) -> int:
        
    #     def _backtrack(idx: int, amount: int, amtOfCoins:int ) -> int:
            
    #         if idx < 0:
    #             return -1

    #         if amount == 0:
    #             return amtOfCoins
    #         elif amount > 0:
    #             amount -= coins[idx]
    #             amtOfCoins += 1
    #         else:
    #             amount < 0
    #             amount += coins[idx]
    #             amtOfCoins -= 1
    #             idx -= 1
            
    #         amtOfCoins = _backtrack(idx, amount, amtOfCoins)
            
    #         return amtOfCoins
        
    #     N = len(coins) - 1

    #     coins.sort()
    #     amtOfCoins = 0
    #     result = _backtrack(N, amount, amtOfCoins)
    #     return result

    def coinChange(self, coins: list[int], amount: int) -> int:
        pass


s = Solution()
print(s.coinChange([186,419,83,408], 6249))
# print(s.coinChange([2,5,10,1], 27))
# print(s.coinChange([1], 0))
# print(s.coinChange([1,2,5], 11))
# print(s.coinChange([1,2,5], 4))
# print(s.coinChange([1,2,5], 3))