from typing import List

class Solution:

    # brute force - time limit exceeded 
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        # brute force try each capacity/total weights to set for ship to take in per day
        low = max(weights)
        high = sum(weights)
        capacity = 0

        def daysNeededByCapacity(capacity):
            daysNeeded = 1
            currTotalWeight = 0

            for x in range(len(weights)):
                if (currTotalWeight + weights[x]) <= capacity:
                    currTotalWeight += weights[x]
                else:
                    daysNeeded += 1
                    currTotalWeight = weights[x]
            
            return daysNeeded

        # brute force try capacity
        for cap in range(low, high + 1):

            daysNeeded = daysNeededByCapacity(cap)

            if daysNeeded == days:
                return cap
            
        return low

s = Solution()
# print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
# print(s.shipWithinDays([3,2,2,4,1,4], 3))
print(s.shipWithinDays([1,2,3,1,1], 4))
