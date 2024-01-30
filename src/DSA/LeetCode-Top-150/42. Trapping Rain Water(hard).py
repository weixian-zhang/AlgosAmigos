from typing import List

class Solution:
    # wrong solution
    def trap(self, height: List[int]) -> int:

        N = len(height)
        water = 0

        if N == 1:
            return 0
        
        left, right = 0, 1

        while left < N - 2:
            
            # if first bar is 0 height
            if left == 0 and height[0] == 0:
                left += 1
                right += 2

            # right bar is either same height or taller than left bar, and with a 1 bar gap at least
            if right <= N -1 and height[right] >= height[left] and (right - left) >= 1:
                
                # calc units of water trapped
                tempLeft = left
                tempRight = right

                if height[tempLeft] < height[tempRight]:
                
                    while tempLeft < tempRight - 1:
                        water += height[left] - height[tempLeft + 1]
                        tempLeft += 1
                else:
                    while tempRight > tempLeft + 1:
                        water += height[right] - height[tempRight - 1]
                        tempRight -= 1

                left = right
                right += 2

            else:
                right += 1

            # if right has reach end
            if right == N - 1:
                left += 1
                right = left + 1

        return water
    
    # techdose solution - also 2 pointers
    def trap(self, height: List[int]) -> int:
        

        N = len(height)

        if N == 1:
            return 0
        
        water = 0
        maxLeft, maxRight = 0, N-1
        left, right = 1, N-2

        while left <= right:
            
            
            if height[maxLeft] <= height[maxRight]:
                if height[left] <= height[maxLeft]:
                    water += height[maxLeft] - height[left]
                else:
                    maxLeft = left
                
                left += 1
            
            else:
                if height[right] <= height[maxRight]:
                    water += height[maxRight] - height[right]
                else:
                    maxRight = right
                
                right -= 1

        return water



s = Solution()
# print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))