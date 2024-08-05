class Solution:

    def findMinArrowShots(self, points: list[list[int]]) -> int:

        points = sorted(points, key = lambda item: item[1])
        
        pc = points.copy()

        arrowsUsed = 0
        while len(pc) > 0:

            pointToShoot = pc[0][1]

            arrowsUsed += 1

            while len(pc) > 0 and pc[0][0] <= pointToShoot <= pc[0][1]:
                pc.pop(0)

        return arrowsUsed


s = Solution()
print(s.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(s.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(s.findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))