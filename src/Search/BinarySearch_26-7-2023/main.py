import math

def binary_search(nums, target):
    
    return binary_search_internal(nums, target, 0, len(nums) - 1)

def binary_search_internal(nums, target, low, high):
    if low >= high:
        return -1

    mid = math.floor(low+high / 2)
    
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_internal(nums, target, low, mid)
    else:
        return binary_search_internal(nums, target, mid, high)

if __name__ == '__main__':
    
    nums = [1,3,5,7,9,11,13]
    target = 5
    
    print(binary_search(nums,target))
    