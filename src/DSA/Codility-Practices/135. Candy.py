from typing import List

# neetcode explanation
# Runtime: 119 ms, faster than 97.13% of Python3 online submissions for Candy.
# Memory Usage: 20.6 MB, less than 11.84% of Python3 online submissions for Candy.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        N = len(ratings)

        if N == 1:
            return 1
        
        candies = [1] * N

        # left to right
        for x in range(1, N):
            if ratings[x] > ratings[x - 1] and candies[x] <= candies[x - 1]:
                # while candies[x] <= candies[x - 1]:
                #     candies[x] += 1
                candies[x] = candies[x - 1] + 1

        # right to left
        for x in range(N - 2, -1, -1):
            if ratings[x] > ratings[x + 1] and candies[x] <= candies[x + 1]:
                # while candies[x] <= candies[x + 1]:
                #     candies[x] += 1
                candies[x] = candies[x + 1] + 1

        return sum(candies)
    
s = Solution()

print(s.candy([1,2,87,87,87,2,1]))
print(s.candy([1,3,2,2,1]))
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))