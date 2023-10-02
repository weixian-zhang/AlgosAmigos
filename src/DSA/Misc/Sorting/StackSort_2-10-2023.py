

def stack_sort(nums):


    tempStack = []
    
    tempNum = 0
    
    item = nums.pop(0)
    
    while item is not None:
        
        if len(tempStack) == 0:
            tempStack.append(item)
        
        else:
            
            largest = item
            
            while len(tempStack) > 0 and tempStack.copy().pop(0) < largest:  
                nums = [tempStack.pop(0)] + nums
                    
            tempStack = [largest] + tempStack
        
        if len(nums) > 0:
            item = nums.pop(0)
        else:
            item = None
        
    return tempStack


if __name__ == '__main__':
    
    print(stack_sort([100,92,6,31,3,55])) #[23,92,98,31,3,24]