namespace _41.FirstMissingPositive;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {

        var s = new Solution();

        //int[] nums = new int[] {3,4,-1,1};

        int[] nums = new int[] {1,2,2,3,10,2147483647,9};

        s.FirstMissingPositive(nums);
    }
}

public class Solution {
    public int FirstMissingPositive(int[] nums) {
        
        if(nums.Length == 1) {

            int singleNum = nums[0];

            if (singleNum == 0 || singleNum == int.MaxValue)
            {
                return 1;
            }
        }

        var positiveOnly = nums.Where(x => x > 0).ToHashSet();

        if(positiveOnly.Count == 0)
            return 1;
        
        var sorted = positiveOnly.OrderBy(x => x).ToList();
        
        int lastNumber = sorted[sorted.Count - 1];

        if(lastNumber != int.MaxValue)
        {
            lastNumber = lastNumber + 1;
        }

        int result = 0;

        foreach(int x in Enumerable.Range(1, lastNumber))
        {
            //fullNumberRange.Add(x);

            if(!sorted.Contains(x))
            {
                result = x;
                break;
            }
        }

        return result;

    }
}