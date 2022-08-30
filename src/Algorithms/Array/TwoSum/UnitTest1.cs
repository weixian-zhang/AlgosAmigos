using System.Collections;

namespace TwoSum;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();

        var nums = new int[] {2,7,9,11,15};
        int target = 9;

        int[] r = s.TwoSum(nums, target);
        Console.WriteLine(r);
    }
}

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        var tracker = new Hashtable();
        
        for(int i = 0; i <= nums.Length; i++) {
            int currentNumber = nums[i];
            int diff = target - currentNumber;
            
            if(tracker.ContainsKey(diff))
                return new int[] { (int)tracker[diff], i };
            else
                tracker[currentNumber] = i; // stores number + index 2,0, 7,1
        }
        
        return new int[] { 0, 0 };
    }
}