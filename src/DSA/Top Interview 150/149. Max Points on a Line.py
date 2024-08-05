from typing import List
from collections import defaultdict

class Solution:
    
    # neetcode explanation
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) <= 2:
            return len(points)
        
        def get_slope(ptA, ptB):
            x1, y1 = ptA[0], ptA[1]
            x2, y2 = ptB[0], ptB[1]

            x = x2 - x1

            if x == 0:
                return float('inf')

            return (y2 - y1) / x
        
        P = len(points)
        max_points = 1
        
        for i in range(P):

            pointI = points[i]
            slopes = defaultdict(lambda: 1, {})

            for j in range(i + 1, P):

                pointJ = points[j]

                slope = get_slope(pointI, pointJ)

                slopes[slope] += 1

                max_points = max(max_points, slopes[slope])

        return max_points

    
s = Solution()

print(s.maxPoints([[1,1],[2,2],[3,3]]))
print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
