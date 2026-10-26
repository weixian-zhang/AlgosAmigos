
# 1 <= prices.length <= 10
# if profit is negative return 0

class Solution:

    def maxProfit(self, prices: list[int]):

        lowest = prices[0]
        profit = 0

        for price in prices:
            lowest = min(price, lowest)
            profit = max(price - lowest, profit)

        return profit

    # Sliding window don't work. 
    # def maxProfit(self, prices: list[int]):

    #     if len(prices) == 1:
    #         return 0

    #     l = len(prices)
    #     windows_size = 3
    #     min_num, max_num = 20, 0


    #     minIdx = 0
    #     maxIdx = minIdx + windows_size

    #     for x in range(l):
            
    #         min_num = min(prices[x:maxIdx])
    #         minIdx = prices.index(min_num)
    #         maxIdx = minIdx + windows_size
    #         max_num = max(prices[minIdx:maxIdx])

    #         # minIdx += 1
    #         maxIdx = minIdx + windows_size

    #     r = min_num - max_num

    #     if r < 0:
    #         return abs(r)
    #     return 0


s = Solution()
print(s.maxProfit([2,4,1]))
#print(s.maxProfit([7,1,5,3,6,4]))
#print(s.maxProfit([7,6,5,4,3]))
#print(s.maxProfit([10,8,5,2,1,2]))


import unittest

class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.s = Solution()

    # 10, 8, 5, 2, 1, 2
    def test_10_8_5_2_1_2(self):
        r = self.s.maxProfit([10, 8, 5, 2, 1, 2])
        self.assertEqual(r, 1)

    # 8,6,3,1,1

    # 8,8,8,8

    # 1, 1,1,1,1,10

    # 10