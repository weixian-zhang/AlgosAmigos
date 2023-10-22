


def binary_search_iterative(nums: list[int], target: int) -> int:
    
    left, right = 0, len(nums)-1
    
    while left <= right:
        
        mid = (right + left) // 2
        
        if nums[mid] > target:
            right = mid  -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
        
    return -1

def binary_search_recursive(nums: list[int], target: int) -> int:
    
    def _recurse(left, right):
        
        if left > right:
            return -1
        
        mid = (right + left) // 2
        
        if nums[mid] > target:
            return _recurse(left, mid - 1)
        elif nums[mid] < target:
            return _recurse(mid + 1, right)
        else:
            return mid
        
        
        
        
    return _recurse(0, len(nums)-1)
        
    
    

    
print(binary_search_iterative([4,7,11,34,45,65,87,99], 101))

print(binary_search_recursive([4,7,11,34,45,65,87,99], 101))