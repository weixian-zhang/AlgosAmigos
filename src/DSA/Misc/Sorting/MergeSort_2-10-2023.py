
def merge_sort(nums: list[int]):

    def _merge(left: list, right: list) -> list:
        
        merged = []

        i, j = 0, 0

        while i <= len(left) - 1 and j <= len(right) - 1:
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged += left[i:]

        merged += right[j:]

        return merged

    def _merge_sort(nums: list) -> list:

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2

        left = nums[:mid]

        right = nums[mid:]

        left = _merge_sort(left)

        right = _merge_sort(right)

        merged = _merge(left, right)

        return merged
    
    sortedNums = _merge_sort(nums)

    return sortedNums

        

    




print(merge_sort([2,8,5,3,9,4,1,7]))