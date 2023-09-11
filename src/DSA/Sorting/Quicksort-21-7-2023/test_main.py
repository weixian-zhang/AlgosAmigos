

import pytest
from main import quicksort

nums_1 = [3,6,8,3,1,5,7,9,4]
nums_2 = [2131,44,66,3,2,644,22,5,5755,97]
nums_3 = [223,321,4,2,1,5,76,66,3]

@pytest.mark.parametrize('nums', [nums_1, nums_2, nums_3])
def test_quicksort_1(nums):
    
    quicksort(nums)
    
    #sliding window so i loop
    for i in range(len(nums) - 1):
        j = i + 1   # window size
        
        assert nums[j] >= nums[i]

if __name__ == "__main__":
    pytest.main(['test_main.py', '-s'])
            

