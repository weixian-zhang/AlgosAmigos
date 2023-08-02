namespace _287.Find_the_Duplicate_Number;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var nums = new int[] { 1,3,4,2,2};

        var s = new Solution();

        int duplicateNum = s.FindDuplicate(nums);
    }
}


public class Solution {
    private HashSet<int> numTracker = new HashSet<int>();

    public int FindDuplicate(int[] nums) {
        
        foreach(int num in nums) {

            if (!numTracker.Add(num)) {
                return num;
            }
        }

        return 0;
    }
}