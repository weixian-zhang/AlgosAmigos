namespace _198.HouseRobber;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var nums = new int[] {100,2,3,4,10,100};

        var s = new Solution();

        int money = s.Rob(nums);
    }
}

//https://www.youtube.com/results?search_query=198.+house+robber
public class Solution {
    public int Rob(int[] nums) {

        if(nums == null || nums.Length == 0)
            return 0;

        if(nums.Length == 2)
            return Math.Max(nums[0], nums[1]);

        int[] maxBucket = new int[nums.Length + 1];
        maxBucket[0] = 0;
        maxBucket[1] = nums[0];

        //2,7,9,3,1
        for(int i = 1; i < nums.Length; i++)
        {
            int currentNumber = nums[i];
            int previousMax = maxBucket[i-1];
            int currentMax = maxBucket[i];

            //calculate next max
            maxBucket[i+1] = Math.Max(currentMax,  previousMax + currentNumber);
        }

        return maxBucket[maxBucket.Length - 1];
        
    }
}