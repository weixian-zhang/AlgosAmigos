class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        result = []
        def backtrack(tempSum: list[int], idx: int):
            
            # base cases
            if sum(tempSum) > target:
                return
            if sum(tempSum) == target:
                result.append(tempSum.copy())
                return
            
            for idx in range(len(candidates)):

                tempSum.append(candidates[idx])

                backtrack(tempSum, idx)

                tempSum.pop()

        backtrack([], 0)

        return result

s =Solution()
s.combinationSum([2,3,5], 8)
s.combinationSum([2,3,6,7], 7)