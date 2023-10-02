
def merge_sort(nums):
    
    
    def _merge_sort(nums):
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        
        left = _merge_sort(nums[:mid])
        
        right = _merge_sort(nums[mid:])
        
        return _sort(left, right)
    


    def _sort(left, right) -> list[int]:
        
        temp = []
        i, j = 0, 0
        
        while i <= len(left)-1 and j <= len(right)-1:
            
            if left[i] <= right[j]:
                temp.append(left[i])
                i += 1
            elif right[j] <= left[i]:
                temp.append(right[j])
                j += 1
                
        
        # add leftover from left to temp
        while i <= len(left)-1:
            temp.append(left[i])
            i += 1
            
        # add leftover from right to temp
        while j <= len(right)-1:
            temp.append(right[j])
            j += 1
            
        
        return temp
    
    return _merge_sort(nums)


if __name__ == '__main__':
    
    print(merge_sort([100,92,6,31,3,55])) #[23,92,98,31,3,24]