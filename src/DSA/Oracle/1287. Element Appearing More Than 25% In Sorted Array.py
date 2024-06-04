from typing import List
import math

class Solution:

    # O(n) solution
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        occurence25P = int(0.25 * len(arr)) + 1
        prevNum = 0
        tfpc = occurence25P

        for n in arr:
            
            if n != prevNum:
                tfpc = occurence25P - 1
                prevNum = n
            else:
                tfpc -= 1

            if tfpc == 0:
                return n
            
        return prevNum
    
    # example for 9 numbers 25% is any 3 occurences.
    # for each number, if number position + 3 = number, then this number appears 25%
    def findSpecialInteger(self, arr: List[int]) -> int:

        occurence25P = int(0.25 * len(arr)) + 1

        for x in range(len(arr)):
            if arr[x + occurence25P - 1] == arr[x]:
                return arr[x]
            
        return arr[-1]

    

    # log(n) - binary search
    # def findSpecialInteger(self, arr: List[int]) -> int:

    #     def binary_Search(x, l, h):
    #         while l <= h:

    #             mid = (h + l) // 2

    #             if arr[mid] == x:
    #                 return mid
                
    #             if arr[mid] > x:
    #                 h = mid - 1
    #             else:
    #                 l = mid + 1
    #         return -1
        
    #     A = len(arr)
    #     occurence25P = int(0.25 * len(arr)) + 1

    #     for x in range(len(arr)):
    #         currNum = arr[x]

    #         idxOfNextOccurence = binary_Search(currNum, x + 1 if x + 1 <= len(arr) else x, A-1)

    #         if idxOfNextOccurence == -1:
    #             continue

    #         if ((idxOfNextOccurence - x) + 1) >= occurence25P:
    #             return currNum

    #     return arr[-1]


s = Solution()
print(s.findSpecialInteger([1,1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]))
# print(s.findSpecialInteger([1,2,2,6,6,6,6,7,10]))
# print(s.findSpecialInteger([1,1]))