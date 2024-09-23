from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        L = len(prices)
        profit = 0
        left, right = 0, 1

        while left != L and right != L:

            if prices[left] <= prices[right]:
                profit = max(prices[right] - prices[left], profit)
                right += 1
            else:
                left = right
                right = left + 1

        return profit
    
s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))