using System;
using System.Collections.Generic;
using Xunit;

namespace QuickSort;

public class QuickerSorter
{
    List<int> result = null;

    public int[] Sort(int[] nums)
    {
        if(result == null)
            result = new List<int>();

        //base case: array size reduced until 0 or 1
        // 0 means all values larger than pivot
        // this mean array contains single value either smallest or biggest as per recursion
        // as array size keep reducing
        if(nums.Length < 2) {
            result.AddRange(nums);
            return nums;
        }

        int pivotIndex = GetPivot(nums);

        int pivotValue = nums[pivotIndex];
        var left = new List<int>();
        var right = new List<int>();
        
        for(int i = 0; i < nums.Length; i++)
        {
            if(nums[i] < pivotValue)
                left.Add(nums[i]);

            if(nums[i] > pivotValue)
                right.Add(nums[i]);
        }

        Console.WriteLine($"pivotValue: {pivotValue}");
        Console.WriteLine($"nums: {string.Join(",", nums)}");
        Console.WriteLine($"left: {string.Join(",", left)}");
        Console.WriteLine($"right: {string.Join(",", right)}");
        Console.WriteLine($"result: {string.Join(",", result)}");
        Console.WriteLine("----------------------");

        //merge pivot value         
        Sort(left.ToArray());

        result.Add(pivotValue);

        Sort(right.ToArray());

        return result.ToArray();
    }

    private int GetPivot(int[] nums)
    {
        int length = nums.Length - 1;
        int pivot = Convert.ToInt32(Math.Floor((decimal)length / 2));
        return pivot;
    }
}

public class UnitTest1
{
    [Theory]
    [InlineData(new int[] {29, 2, 1, 77, 63, 28} )]
    public void Test_QuickSort(int[] nums)
    {
        var sorter = new QuickerSorter();

        int[] sorted = sorter.Sort(nums);

        Console.WriteLine(string.Join(", " , sorted));
    }
}