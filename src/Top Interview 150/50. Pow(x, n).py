class Solution:

    # python default power
    # Runtime: 40 ms, faster than 38.98% of Python3 online submissions for Pow(x, n).
    # Memory Usage: 16.6 MB, less than 64.89% of Python3 online submissions for Pow(x, n).
    def myPow(self, x: float, n: int) -> float:
        return x ** n
    

    # brute force - O(N) - error Maximum recursion epth exceeded due to N = 2**31
    def myPow(self, x: float, n: int) -> float:

        isNegative = False if n > 0 else True
        n = abs(n)
        
        result = x
        def recurse(multiplyByTimes: int):
            nonlocal result

            if multiplyByTimes == n:
                return 1
            
            return x * recurse(multiplyByTimes + 1)
        
        powResult = recurse(0)

        if isNegative:
            return 1 / powResult
        
        return powResult
    
    # binary exponential - iterative
    # Runtime: 30 ms, faster than 91.71% of Python3 online submissions for Pow(x, n).
    # Memory Usage: 16.7 MB, less than 58.25% of Python3 online submissions for Pow(x, n).
    def myPow(self, x: float, n: int) -> float:

        base, exponent = x, abs(n)
        
        isNegative = False if n > 0 else True
        n = +n

        # binary expoential
        result = 1
        while exponent > 0:


            if exponent % 2 == 1:
                result *= base
                exponent -= 1
            else:
                base *= base
                exponent /= 2

        if isNegative:
            result = 1 / result

        return result
    

# binary expoential with recursion
# Runtime: 38 ms, faster than 53.52% of Python3 online submissions for Pow(x, n).
# Memory Usage: 16.8 MB, less than 54.53% of Python3 online submissions for Pow(x, n).
class Solution:
    def myPow(self, x: float, n: int) -> float:

        isNegative = n < 0
        # convert negative to positive
        if isNegative:
            n = -1 * n

        def recurse_bin_exponential(x, n, result):

            # Base case, to stop recursive calls.
            if n == 0:
                return 1
            
            # if exponent n == 1, return base x 
            if n == 1:
                return x
            
            # even
            if n % 2 == 0:
                result = recurse_bin_exponential(x * x, n // 2, result)

            # odd
            else:
                result = x * recurse_bin_exponential(x * x, (n - 1) // 2, result)

            return result
            
        result = recurse_bin_exponential(x, n, 1)

        return result if not isNegative else 1 / result
        


s = Solution()
print(s.myPow(2, 10))
print(s.myPow(x = 2.00000, n = -2))
# print(s.myPow(x = 2.00000, n = 10))

        