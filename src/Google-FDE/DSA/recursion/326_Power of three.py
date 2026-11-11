
# https://leetcode.com/problems/power-of-three/description/?envType=problem-list-v2&envId=recursion

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        def recursion(power: int = 0):

            result = 3 ** power

            if result == n:
                return True

            if result > n:
                return False

            power += 1

            return recursion(power)

        
        return recursion()
    

s = Solution()
print(s.isPowerOfThree(9))


            