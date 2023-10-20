import math
class Solution:
    
    # binary search
    def mySqrt(self, x: int) -> int:
        
        result = 0
        left, right = 0, x // 2
        
        while left <= right:
            
            mid = left + ((right - left) // 2)
            
            if mid ** 2 > x:
                right = mid  - 1
                
            elif mid ** 2 < x:
                left = mid + 1
            else:
                return mid
            
        return right
            
                
    
    # brute force
    # def mySqrt(self, x: int) -> int:
        
    #     if x == 1:
    #         return 1
        
    #     result = 0

    #     for n in range(1, x+1):
    #        if n * n > x:
    #            result = n - 1
    #            break
        
    #     return result
    
    
        
    
    
    
    
if __name__ == '__main__':
    
    s = Solution()
    #print(s.mySqrt(1))
    #print(s.mySqrt(1125))
    print(s.mySqrt(8))
    #print(s.mySqrt(49))