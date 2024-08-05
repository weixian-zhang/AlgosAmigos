class Solution:

    # Runtime: 4092 ms, faster than 12.78% of Python3 online submissions for Factorial Trailing Zeroes.
    # Memory Usage: 16.7 MB, less than 56.51% of Python3 online submissions for Factorial Trailing Zeroes.
    def trailingZeroes(self, n: int) -> int:
        import sys
        sys.set_int_max_str_digits(0)

        zeros = 0
        r = 1
        for x in range(1, n + 1):
            r *= x

        #string count method
        r = str(r)
        for s in range(len(r) - 1, -1, -1):
            if r[s] == '0':
                zeros += 1
            else:
                break

        return zeros

    # Runtime: 9566 ms, faster than 5.05% of Python3 online submissions for Factorial Trailing Zeroes.
    # Memory Usage: 16.6 MB, less than 56.51% of Python3 online submissions for Factorial Trailing Zeroes.
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        r = 1
        for x in range(1, n + 1):
            r *= x
            
        divisableBy10 = True
        while divisableBy10:
            
            if r % 10 == 0:
                r = r // 10
                zeros += 1
            else:
                divisableBy10 = False

        return zeros
    
    # optimial - divide by 5 method
    # 5! = 1 zero, 10! = 2 zero, 15! = 3, 25! = 6
    # just divide by 5 to get the resulting zeros
    def trailingZeroes(self, n: int) -> int:

        zeros = 0

        while n > 0:
            n = n // 5
            zeros += n 
            
        return zeros
    

s = Solution()
# print(s.trailingZeroes(5))
# print(s.trailingZeroes(10))
print(s.trailingZeroes(15))
print(s.trailingZeroes(20))
# print(s.trailingZeroes(1574))
# print(s.trailingZeroes(3))
# print(s.trailingZeroes(5))