


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:

        def recursion(val: int, power: int) -> bool:

            val = 2 ** power

            if val == n:
                return True
            
            if power > 31:
                return False

            return recursion(val, power + 1)

        return recursion(0, 0)
    

    def _isPowerOfTwo(self, n: int) -> bool:
        
        for x in range(31):
            if 2 ** x == n:
                return True

        return False



s = Solution()
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(1))