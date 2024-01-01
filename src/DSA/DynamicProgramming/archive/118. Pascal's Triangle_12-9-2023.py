class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        
        result = []
        
        def _recurse(n, nums):
            
            if n == numRows + 1:
                return
                       
            # initializing the first 2 rows of Pascal Triangle
            if n == 1:
                nums = [n]
                result.append(nums)
            elif n == 2:
                nums = [1,1]
                result.append(nums)
                
            # actual computation here 
            else:
                temp = [1]
                windows_size = 1
                
                #sliding window
                for i in range(len(nums) - windows_size):
                        temp += [nums[i] + nums[i + windows_size]]
                        
                temp += [1]
                
                nums = temp.copy()
                
                result.append(nums)
                
            _recurse(n+1, nums)
                

        _recurse(1, [])
        
        return result
    
    
if __name__ == '__main__':
    s = Solution()
    r = s.generate(5)
    print(r)