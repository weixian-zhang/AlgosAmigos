

nums = [2,5,4,7,3]

def find_odd_recursively(nums, idx, result: list):
    
    # base case
    if idx == len(nums) - 1:
        return result
    
    if nums[idx] % 2 != 0:
        result.append(nums[idx])
    
    return find_odd_recursively(nums, idx + 1, result)


if __name__ == '__main__':
    result = find_odd_recursively(nums, 0, result=[])
    print(result)