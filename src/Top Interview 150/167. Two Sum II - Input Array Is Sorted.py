class Solution:
    
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        diffDict = {}
        left, right = 0, len(numbers) - 1
        
        while left <= right:
                
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            
            if numbers[left] in diffDict.values():
                idx1 = left +1
                idx2 = self._get_key_by_val(diffDict, numbers[left]) + 1
                r = [idx1, idx2]
                r.sort()
                return r
            else:
                diffDict[left] = target - numbers[left]
                left += 1
                
            if numbers[right] in diffDict.values():
                idx1 = right + 1
                idx2 = self._get_key_by_val(diffDict, numbers[right]) + 1
                r = [idx1, idx2]
                r.sort()
                return r
            else:
                diffDict[right] = target - numbers[right]
                right -= 1
                    
                
    def _get_key_by_val(self, diffDict: dict, target: int) -> int:
        for k, v in diffDict.items():
            if v == target:
                return k
        return -1
    
    # solution by binary search
    # def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
    #     def _binary_search(low: int, high: int, toFind: int, currIdxToAvoid) -> int:
            
    #         while high >= low:
    #             mid = (low + high) // 2
                
    #             if numbers[mid] > toFind:
    #                 high = mid - 1
    #             elif numbers[mid] < toFind:
    #                 low = mid + 1
    #             else:
    #                 # found, check if it
    #                 return mid
            
    #         return -1
        
    #     for x in range(len(numbers)):
            
    #         bsResult = _binary_search(0, len(numbers) - 1, target - numbers[x], x)
            
    #         if bsResult != -1:
    #             idx1 = x + 1
    #             idx2 = bsResult + 1
                
    #             # check if same index which means duplicate numbers
    #             if idx1 == idx2:
    #                 return [x + 1, bsResult + 2]
    #             else:
    #                 return [x + 1, bsResult + 1]
        
    # solution with 2 pointers store difference
    
    
    
s = Solution()
print(s.twoSum([1,2,3,4,4,9,56,90], 8))
# print(s.twoSum([5,25,75], 100))
# print(s.twoSum([2,7,11,15], 9))
# print(s.twoSum([2,3,4], 6))
# print(s.twoSum([-1, 0], -1))