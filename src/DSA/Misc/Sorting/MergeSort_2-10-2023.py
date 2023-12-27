
def merge_sort(nums: list[int]):

    def merge(left, right):

        merge = []
        i, j = 0, 0
        while i <= len(left) - 1 and j <= len(right) - 1:

            if left[i] <= right[j]:
                 merge.append(left[i])
                 i += 1
            else:
                merge.append(right[j])
                j += 1

        # refactor to use list.extend
        merge.extend(left[i:])
        merge.extend(right[j:])

        return merge
    
    def _mergeSort(nums: list[int]):
        import math

        if len(nums) <= 1:
            return nums
        
        mid =  math.floor(len(nums) // 2)

        left = nums[:mid]

        right = nums[mid:]

        left = _mergeSort(left)

        right = _mergeSort(right)

        return merge(left, right)

        
    return _mergeSort(nums)



print(merge_sort([2,8,5,3,9,4,1,7]))