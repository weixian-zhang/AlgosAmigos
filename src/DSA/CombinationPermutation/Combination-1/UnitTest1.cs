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

        var r1 = s.Combine(4, 2);

        //Assert.True(r1.Count == Math.Pow(2, nums.Length));
    }
}

public class Solution
{
//     public IList<IList<int>> Combine(int n, int k) {
        
//         //init range of numbers
//         var nums = new List<int>();
//         foreach(int x in Enumerable.Range(k, n-1))
//         {
//             nums.Add(x);
//         }

//         var tempResult = new List<List<int>>();
//         int noOfNumsInASetAsAnswer = k;
//         var result = CombineHelper(nums.ToArray(), 0, tempResult, noOfNumsInASetAsAnswer);

//         var rFiltered = result.Where( r => r.Count == 2);

//         IList<IList<int>> ilist = result.Select(x => (IList<int>)x).ToList();

//         return ilist;
// ;
     
//     }

    // private List<List<int>> CombineHelper(int[] nums, int i, List<List<int>> result, int noOfNumsInASetAsAnswer)
    // {
    //     if(nums.Length == 0)
    //     {
    //         result.Add(new List<int>(){});
    //         return result;
    //     }

    //     var firstElement = nums[i];
    //     var slice = nums.Skip(i+1).Take(nums.Length - 1).ToArray();

    //     result = CombineHelper(slice, i, result, noOfNumsInASetAsAnswer);

    //     var mergeNewCombos = new List<List<int>>();
    //     //var newCom = new List<int>();
    //     foreach(var r in result)
    //     {
    //         var newCombo = new List<int>(r);

    //         newCombo.AddRange(new List<int>(){firstElement});

            
    //         mergeNewCombos.Add(newCombo);
    //     }

    //     result.AddRange(mergeNewCombos);

    //     return result;
        
    // }














    




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