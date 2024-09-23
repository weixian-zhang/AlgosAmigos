class Solution:
    
    # take the "next" price minus previous price as long as "next" price is larger than previous price
    def maxProfit(self, prices: list[int]) -> int:
        
        maxProfit = 0
        
        i = 1
        while i <= len(prices) - 1:
            
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]

            i += 1
                
        return maxProfit
    
    # my solution time exceeded - using matrix of profit with recursion
    # def maxProfit(self, prices: list[int]) -> int:
        
    #     maxProfit = 0
    #     tempProfit = 0
        
    #     # build a profit matrix
    #     matrix = self._build_profit_matrix(prices)
    #     columnLength = len(matrix[0])
        
        
    #     def _traverse_matrix_recursive(startRow, startCol):
    #         nonlocal tempProfit, maxProfit
            
    #         # base case
    #         if startRow > (len(matrix) - 1) or startCol > (columnLength - 1):
    #             return
        
    #         # get max profit from matrix
    #         for i in range(startRow, len(matrix)):
    #             for j in range(startCol, columnLength):
    #                 if matrix[i][j] <= 0:
    #                     continue
                    
    #                 #set the profit
    #                 tempProfit += matrix[i][j]
                    
    #                 _traverse_matrix_recursive(j+1, j+1)
                    
    #                 maxProfit = max(maxProfit, tempProfit)
                    
    #                 # backtrack to previous "cell" and minus off previous profit and try the next project
    #                 tempProfit -= matrix[i][j]
                
                    
    #     _traverse_matrix_recursive(0,0)
        
    #     return maxProfit
                
                
    # def _build_profit_matrix(self, prices: list[int]):
        
    #     matrix = []
        
    #     for _ in range(len(prices)):
    #         matrix.append([0 for x in range(len(prices))])
        
    #     for i in range(len(prices)):
    #         for j in range(i+1, len(prices)):
    #                 matrix[i][j] = prices[j] - prices[i]
                
    #     return matrix

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
# print(s.maxProfit([1,2,3,4,5]))
# print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([6,1,3,2,4,7]))