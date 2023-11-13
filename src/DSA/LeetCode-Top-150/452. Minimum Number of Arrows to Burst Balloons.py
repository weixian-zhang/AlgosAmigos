class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        
        overlapCount = 0
        l, r = 0, 1

        points = sorted(points, key = lambda item: item[0])

        while r <= len(points) - 1:
            
            if self._is_overlap(points[l], points[r]):
                overlapCount += 1
                r += 1
            else:
                l = r

            if l == r:
                r += 1
            

        return len(points) - overlapCount

    def _is_overlap(self, a: list[int], b: list[int]):
        x1, x2 = a[0], a[1]
        y1, y2 = b[0], b[1]
        return y1 <= x2 and x1 <= y2


s = Solution()
#print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
# print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))