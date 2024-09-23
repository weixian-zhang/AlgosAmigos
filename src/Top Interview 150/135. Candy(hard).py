from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        N = len(ratings)

        candies = [1] * N

        # left to right check is current rating bigger than right neighbour
        for x in range(1, N):
            if ratings[x] > ratings[x - 1]:
                candies[x] = max(candies[x], candies[x - 1]) + 1

        for x in range(N-2, -1, -1):
            if ratings[x] > ratings[x + 1] and candies[x] <= candies[x + 1]:
                candies[x] = max(candies[x + 1], candies[x]) + 1

        return sum(candies)
    


s = Solution()
print(s.candy([1,2,87,87,87,2,1]))
print(s.candy([1,0,2]))
print(s.candy([1,2,2]))

