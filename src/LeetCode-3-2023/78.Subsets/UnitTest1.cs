namespace _78.Subsets;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();

        var combos = s.Subsets(new int[] { 1,2,3,4,5,6,7,8,10,0});
    }
}


public class Solution {

    private List<IList<int>> result = new List<IList<int>>();

    private HashSet<List<int>> tempResult = new HashSet<List<int>>(new ListIntComparer());

    public IList<IList<int>> Subsets(int[] nums) {
        
        var combination = new List<int>();

        Backtrack(nums);

        result.AddRange(tempResult);

        return result;
    }

    private int[] Backtrack(int[] nums)
    {
        //base case
        if (nums.Length == 0) {
            tempResult.Add(EmptyIntList());
            return new int[]{};
        }

        tempResult.Add(nums.ToList());

        for(int idx = 0; idx < nums.Length; idx++) {
            
            var numList = new List<int>(nums[idx]);
            bool added = tempResult.Add(numList);

            var newNums = new List<int>(nums);
            newNums.RemoveAt(idx);

            Backtrack(newNums.ToArray());
        }

        return nums;
    }

    private List<int> EmptyIntList() {
        return new List<int>();
    }

    private List<int> NumToList(int num) {
        return (new int[] { num}).ToList();
    }

}

public class ListIntComparer : IEqualityComparer<List<int>>
{
    public bool Equals(List<int> x, List<int> y)
    {
        string xStr = string.Join("", x);
        string  yStr = string.Join("", y);
        return xStr == yStr;
    }

    public int GetHashCode(List<int> listInt)
    {
        return string.Join("", listInt).GetHashCode();
    }
}