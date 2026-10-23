
class Solution:

    def find_subsets(self, nums: list[int]):

        result = []

        def backtrack(index, current_subset):
            # Base Case: If we've made a choice for every element, save the result
            if index == len(nums):
                result.append(current_subset.copy()) # copy is required to preserve state
                return
                
            # Decision 1: Include nums[index]
            current_subset.append(nums[index])
            backtrack(index + 1, current_subset)
            
            # Decision 2: Exclude nums[index] (Backtrack step)
            current_subset.pop() # Remove the last element before branching
            backtrack(index + 1, current_subset)

        # Start the backtracking algorithm from index 0 with an empty list
        backtrack(0, [])
        return result



# Example Execution
nums = [1, 2, 3]
s = Solution()
print(s.find_subsets(nums))