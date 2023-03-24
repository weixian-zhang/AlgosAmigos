namespace _46.Permutation;
using System.Collections.Generic;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var solution = new Solution();
        var result = solution.Permute(new int[] {1 ,2, 3});
    }
}


public class Solution {


    public IList<IList<int>> Permute(int[] nums) {

        var result = new List<IList<int>>();

        Backtrack(result, new List<int>(), nums);

        return result;
    }

     private void Backtrack(List<IList<int>> result, List<int> permutation, int[] nums)
     {
        if (permutation.Count == nums.Length) {
            result.Add(permutation.ToList());
            return;
        }

        // if (result.Count == FactorialOf(nums.Length)) {
        //     return;
        // }

        foreach(int num in nums)
        {
            if(permutation.Contains(num))
                continue;

            permutation.Add(num);

            Backtrack(result ,permutation, nums);

            //permutation.Clear();

            int idxToRemove = permutation.Count - 1;
            permutation.RemoveAt(idxToRemove);
        }


        return;
     }

     private int FactorialOf(int num) {
        int fac = 1;
        for(int i = 1; i<= num; i++)
        {
            fac *= i;
        }
        return fac;
     }

     private List<int> CopyWithExclude(int[] nums, int indexToExclude)
     {
        var newNums = nums.Where(i => true).ToList();
        newNums.RemoveAt(indexToExclude);
        return newNums;
     }

}