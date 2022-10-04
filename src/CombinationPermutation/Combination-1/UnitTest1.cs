namespace Combination_1;

public class UnitTest1
{
    [Theory]
    [InlineData(new int[]{1,2,3})]
    [InlineData(new int[]{1,2})]
    [InlineData(new int[]{5,7,8,9})]
    public void Test1(int[] nums)
    {
        var s = new Solution();

        var r1 = s.GenerateCombinations(nums);

        Assert.True(r1.Count == Math.Pow(2, nums.Length));
    }
}

public class Solution
{
    public List<List<int>> GenerateCombinations(int[] nums)
    {
        List<List<int>> result = new List<List<int>>();

        result =  GenerateCombinations(nums, 0, result);

        return result;
    }

    private List<List<int>> GenerateCombinations(int[] nums, int i, List<List<int>> result)
    {
        List<int> combo = new List<int>();

        if(nums == null || nums.Length == 0)
        {
            result.Add(new List<int>(){});
            return result;
        }

        var firstElement = nums[i];
        var slice = nums.Skip(i + 1).Take(nums.Length - 1).ToArray();


        result = GenerateCombinations(slice, i, result);

        var  mergeNewCombos = new List<List<int>>();

        foreach (List<int> r in result)
        {
            var newCombo = new List<int>(r);
        
            newCombo.AddRange(new List<int>(){firstElement});

            mergeNewCombos.Add(newCombo);
        }

        result.AddRange(mergeNewCombos);
        return result;
    }
}