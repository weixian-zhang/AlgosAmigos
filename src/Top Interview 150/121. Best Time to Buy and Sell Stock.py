class Solution:
    
    # 2 pointers
    def maxProfit(self, prices: list[int]) -> int:
        
        leftBuy, rightSell = 0, 1
        maxProfit = 0
        
        while leftBuy <= rightSell and rightSell <= (len(prices) - 1):
            
            if prices[rightSell] < prices[leftBuy]:
                leftBuy = rightSell
                rightSell += 1
            else:
                maxProfit = max(maxProfit, prices[rightSell] - prices[leftBuy])
                rightSell += 1
                
        return maxProfit
    
    # brute force, exceed time limit
    # def maxProfit(self, prices: list[int]) -> int:
    
        
    #     def _recurse(prices, buyIdx, buyPrice, maxProfit) -> int:
            
    #         if buyIdx > len(prices) - 1:
    #             return maxProfit
            
    #         buyPrice = prices[buyIdx]
            
    #         sellDays = [x for x in prices[buyIdx+1:] if x > buyPrice]
            
    #         for x in range(len(sellDays)): #range(buyIdx + 1, len(prices)):
                
    #             sellPrice = sellDays[x]
                
    #             if sellPrice > buyPrice:
                    
    #                 diff = sellPrice - buyPrice
                    
    #                 if diff > maxProfit:
    #                     maxProfit = diff
                    
                    
    #         return _recurse(prices, buyIdx + 1, buyPrice, maxProfit)
        
        
    #     dayToSell = _recurse(prices, 0,0,0)
        
    #     return dayToSell
            
    

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,6,4,1,8]))  #[7,6,4,3,1])) #[7,1,5,3,6,4]))