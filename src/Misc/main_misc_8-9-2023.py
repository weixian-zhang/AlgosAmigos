
class Recursions:
    
    def is_in_sequence(self, nums):
        
        def recurse_v1(nums, idx):
            
            if idx + 1 > len(nums) - 1:
                    return True
            
            if nums[idx] + 1 != nums[idx + 1]:
                return False
            
            return recurse_v1(nums, idx + 1)
        
        
        def recurse_v2(nums, idx):

            return (idx + 1 > len(nums) - 1) or (nums[idx] + 1 == nums[idx + 1] and recurse_v2(nums, idx + 1))
            
        
        #ok = recurse_v1(nums, 0)
        
        ok = recurse_v2(nums, 0)
        
        return ok
    
    
    def sum_all_nums(self, nums):
        
        def recurse(nums):
            
            if len(nums) == 1:
                return nums[-1]
            
            return  nums[-1] + recurse(nums[:len(nums) - 1])
            
        
        return recurse(nums)
    
    
    

if __name__ == '__main__':
    recursions = Recursions()
    print(recursions.is_in_sequence([2,3,4,5,6,7]))
    #print(recursions.sum_all_nums([1,2,3,4,5,6]))