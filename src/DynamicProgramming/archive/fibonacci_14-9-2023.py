
class Solution:
    
    def fib_with_memoization(self, fibOf, result):
        
        memoization = { x:-1 for x in range(1,fibOf+1) }
        
        def _recurse(fibOf, result):
            
            if fibOf > 0 and memoization[fibOf] != -1:
                return memoization[fibOf]
            
            if fibOf == 1:
                result = 1
                memoization[fibOf] = result
            elif fibOf == 0:
                result = 0
            else:
                result = _recurse(fibOf - 2, result) + _recurse(fibOf - 1, result)
                memoization[fibOf] = result
        
            return result
        
        return _recurse(fibOf, 0)
    
    
    def fib_with_tabulation(self, fibof):
        
        dp = [0 for x in range(fibof)]
        dp[0] = 1
        dp[1] = 1
        
        for idx in range(2, fibof):
            dp[idx] = dp[idx - 2] + dp[idx - 1]
            
        result = dp[-1]
        
        return result
        
        
    

if __name__ == '__main__':
    
    s = Solution()
    
    r1 = s.fib_with_memoization(8, 0)
    print(r1)
    
    r2 = s.fib_with_tabulation(144)
    print(r2)