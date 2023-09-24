namespace _300.LongestIncreasingSubsequence;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();

        int r = s.LengthOfLIS(new int[] {10,9,2,5,3,7,101,18});
    }
}

public class Solution {

    public int LengthOfLIS(int[] nums) 
    {
        if(nums == null || nums.Length == 0)
            return 0;

        if(nums.Length == 1)
            return 1;

        int[] dp = DPArray(nums);
        int[] dpParent = DPParentArray(nums);

        for(int j = 1; j < nums.Length; j++)
        {
            for(int prev= 0; prev < j; prev++)
            {
                int currentNum = nums[j];
                int prevCompareNum = nums[prev];

                if(currentNum > prevCompareNum)
                {
                    int lengthFromPrevDP = dp[prev];
                    int lengthToIncrease = lengthFromPrevDP + 1;

                    if(lengthToIncrease > dp[j])
                    {
                        dp[j] = lengthToIncrease;
                        dpParent[j] = prev;
                    }
                }
            }
        }

        int[] theNumbers = GetIncreasingNumberChain(dpParent,dp,nums);
        Console.WriteLine(string.Join(",", theNumbers.OrderBy(x => x).ToList()));

        return dp.Max();
    }

    private int[] DPArray(int[] nums)
    {
        var dp = new List<int>();

        foreach(int x in Enumerable.Range(0, nums.Length))
        {
            dp.Add(1);
        }
        return dp.ToArray();
    }

    private int[] DPParentArray(int[] nums)
    {
        var dp = new List<int>();

        foreach(int x in Enumerable.Range(0, nums.Length))
        {
            dp.Add(-1);
        }
        var r = dp.ToArray();
        r[0] = 0;

        return r;
    }

    private int[] GetIncreasingNumberChain(int[] dpParent, int[]dp, int[] nums)
    {
        var result = new List<int>();

        int maxLength = dp.Max();

        int maxIndex = Array.IndexOf(dp, maxLength);

        int indexDiff = dp.Length - maxIndex;

        int skipBackwards = dp.Length - indexDiff;

        //add the max number first
        result.Add(nums[skipBackwards]);

        while(skipBackwards != -1)
        {
           skipBackwards =  dpParent[skipBackwards];

           if(skipBackwards != -1)
                result.Add(nums[skipBackwards]);
        }

        

        return result.ToArray();
    }
}