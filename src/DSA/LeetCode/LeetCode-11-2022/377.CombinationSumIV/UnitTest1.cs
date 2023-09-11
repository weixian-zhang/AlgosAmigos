namespace _377.CombinationSumIV;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();
        s.CombinationSum4(new int[] {1,2,3}, 4);
    }
}


public class Solution {
    public int CombinationSum4(int[] nums, int target) {

        int[] dp = new int[target + 1];
        foreach(int x in Enumerable.Range(0, dp.Length))
        {
            dp[x] = 0;
        }

        dp[0] = 0;

        int combinationCount = 0;

        for (int i = 1; i < dp.Length; i++)
        {
            combinationCount = 0;

            for (int n = 0; n < nums.Length; n++)
            {
                int num = nums[n];

                int remainder = i - num;

                if (remainder == 0)
                {
                    combinationCount++;
                }
                else if( remainder > 0)
                {
                    combinationCount += dp[remainder];
                }
            }
            
            dp[i] = combinationCount;
        }

        int result = dp[target];
        return result;
        
    }
}