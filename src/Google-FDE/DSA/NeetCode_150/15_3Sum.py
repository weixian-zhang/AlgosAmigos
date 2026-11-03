# 3 <= nums.length <= 3000


class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:

        window_size = 3
        size = len(nums)
        nums = sorted(nums)
        tuple_set = set()

        for left in range(size - 2):

            low, high = left + 1, size - 1

            while low <= size - 1 and low != high and high > low:
                three_nums = (nums[left], nums[low], nums[high])
                total = sum(three_nums)

                if total == 0:
                    tuple_set.add(three_nums)
                    low += 1
                    high -= 1

                elif total > 0:
                    high -= 1

                else:
                    low += 1

        nested_list = [list(t) for t in tuple_set]
        return nested_list

    def _threeSum(self, nums: list[int]) -> list[list[int]]:

        nums = sorted(nums)

        size = len(nums) - 1
        mid = len(nums) // 2
        left = mid - 1
        right = mid + 1

        result = set() # contains tuple of 3 nums

        while left >= 0 and right <= size and 0 <= mid <= size:

            curr_sum = sum([nums[left], nums[mid], nums[right]])

            if curr_sum == 0:
                result.add((nums[left], nums[mid], nums[right]))
                left = left - 1
                right = right + 1

            elif curr_sum > 0:
                mid = mid - 1 if mid - 1 >= 0 else 0

            else:
                mid = mid + 1 if mid + 1 <= size else size
                

            left = mid - 1 if mid == left else left - 1
            right = mid + 1 if mid == right else right + 1

        return list(result)


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([-1,0,1,2,-1,-4]))
print(s.threeSum([0,1,1]))
print(s.threeSum([-100,-70,-60,110,120,130,160]))

        



