from typing import List

# Runtime: 43 ms, faster than 84.40% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 17.1 MB, less than 57.68% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(nums: list[int], low: int, high: int):
            
            while low <= high:
                mid = (high + low) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return False
        
        for row in matrix:
            if binary_search(row, 0, len(row) - 1):
                return True
        
        return False
            


s = Solution()

print(s.searchMatrix([[1,3]], 3))

# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))