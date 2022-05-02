using System.Diagnostics;
using Xunit;

namespace SelectionSort;

public class SelectionSorter
{
    public int[] Sort(int[] nums)
    {
        for(int i = 0; i < nums.Length - 1; i ++)
        {
            int currentMinIndex = i;

            for(int x = i + 1; x < nums.Length; x++)
            {
                int currentMin = nums[currentMinIndex];
                int nextVal = nums[x];
                if(nextVal < currentMin) {
                    currentMinIndex = x;
                }
            }

            //means there is number bigger than current i, then swap with x-index value
            if( i != currentMinIndex) {
                int temp = nums[i];
                nums[i] = nums[currentMinIndex];
                nums[currentMinIndex] = temp;
            }
        }

        return nums;
    }
}

public class Test_SelectionSort
{
    [Theory]
    [InlineData(new int[] {29, 2, 1, 77, 63, 28} )]
    [InlineData(new int[] {-89, -3, 1, 0, 22, 99} )]
    [InlineData(new int[] {101, 12, 13, 77, 63, 45} )]
    public void SelectionSort_Asc(int[] nums)
    {
        var sorter = new SelectionSorter();

        int[] sortedNums = sorter.Sort(nums);

        Debug.WriteLine(string.Join(",", sortedNums));
    }
}