class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        
        result = []

        def backtrack(nums: list[int], tempCombo: list[int]):
            
            # base case
            if len(tempCombo) == k:
                result.append(tempCombo.copy())
                return
            
            for idx, x in enumerate(nums):

                tempCombo.append(x)

                backtrack(nums[idx + 1:], tempCombo)

                tempCombo.pop()

        nums = [x for x in range(1, n + 1, 1)]

        backtrack(nums, [])

        return result



s = Solution()
print(s.combine(4, 2))
print(s.combine(1, 1))
print(s.combine(6, 3))