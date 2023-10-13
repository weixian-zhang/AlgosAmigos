class Solution:
    
    # best solution
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        seenNums = set()
        
        sumResult = n
        
        while sumResult != 1 and sumResult not in seenNums:
            
            seenNums.add(sumResult)
            
            sumResult = self.sum_of_square(sumResult)
            
            if sumResult == 1:
                return True
                
        return False
    
    def sum_of_square(self, num):
        nums = []
        for x in str(num):
            nums.append(int(x) ** 2)
        return sum(nums)
    
    # accepted number but not elegant due to trial and error on the number of "tries"
    # def isHappy(self, n: int) -> bool:
        
    #     if n == 1:
    #         return True
        
    #     sumResult = n
    #     numOfLoops = 0
        
    #     while sumResult != 1 and numOfLoops <= 5:
    #         nums = []
    #         for x in str(sumResult):
    #             nums.append(int(x) ** 2)
            
    #         sumResult = sum(nums)
            
    #         numOfLoops += 1
            
    #     return sumResult == 1
    
    
    
if __name__ == '__main__':
    s = Solution()
    #s.isHappy(19)
    #s.isHappy(2)
    s.isHappy(2)