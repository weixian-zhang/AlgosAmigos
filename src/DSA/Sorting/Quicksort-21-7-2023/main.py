

def quicksort(nums):
    
    qs_internal(nums, 0, len(nums) - 1)

    # select last index of array a pivot
    # i index is 0 -1
    # j index is 0
    
    #loop until pivot is in right position

def qs_internal(nums, begin, end):
    
    if begin >= end:
        return
    
    #last index pivot
    currentPivotIdx = end
    
    newPivotIndex = partition(nums, begin, end, currentPivotIdx)
    
    qs_internal(nums, 0, newPivotIndex - 1)
    
    qs_internal(nums, newPivotIndex + 1, end)
    
# get new index of pivot being swapped into position
def partition(nums, begin, end, pivotIdx):
    i = begin - 1
    for j in range(begin, end):
        if nums[j] < nums[pivotIdx]:
            i += 1  # important
            swap(nums, i, j )
    
    i += 1
    swap(nums, i, pivotIdx)
    return i
    

def swap(nums, srcIdx, destIdx):
    temp = nums[srcIdx]
    nums[srcIdx] = nums[destIdx]
    nums[destIdx] = temp
    
if __name__ == '__main__':
    
    nums = [11, 9, 4,111,64, 2, 7, 3, 55, 6]
    
    quicksort(nums)
    
    print(nums)