class Solution:

    def maxArea(self, height: list[int]) -> int:

        maxWaterUnit = 0

        left, right = 0, len(height) - 1
        while left < right:

            waterArea = self.calc_max_water(height, left, right)
            maxWaterUnit = max(maxWaterUnit, waterArea)

            if height[right] > height[left]:
                 left += 1
            elif height[right] < height[left]:
                 right -= 1
            else:
                 left += 1
                 right -= 1
            

        return maxWaterUnit
    
    def calc_max_water(self, height:list[int], left, right):
            width = (right + 1) - (left + 1)
            h = min(height[left], height[right])
            return width * h


    # time exceeded
    # def maxArea(self, height: list[int]) -> int:
        
    #     maxWaterUnit = 0
    #     curr_right_height = 0

    #     for left in range(len(height)):

    #         right = len(height) - 1
    #         while right > left:

    #             width = (right + 1) - (left + 1)

    #             h = min(height[left], height[right])

    #             maxWaterUnit = max(maxWaterUnit, width * h)

    #             right -= 1
        
    #     return maxWaterUnit


s = Solution()
print(s.maxArea([1,3,2,5,25,24,5]))
# print(s.maxArea([2,3,4,5,18,17,6]))
# print(s.maxArea([1,8,6,2,5,4,8,3,7]))
# print(s.maxArea([1,1]))