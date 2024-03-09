class Solution:
    def climbStairs(self, n: int) -> int:

            cache = {}

            def recursion(step: int):
                                
                if step > n:
                    return 0
                
                if step == n:
                    return 1
                
                if step in cache:
                     return cache[step]

                cache[step] = recursion(step + 1) + recursion(step + 2)

                return cache[step]


            ways = recursion(0)

            return ways


s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(5))
# print(s.climbStairs(11))