using System;
using System.Diagnostics;
using FindPairWithSumOfGivenNumber;
using Xunit;

public class Test_FindPairWithSumOfGivenNumber
    {
        [Theory]
        [InlineData(new [] {4, 9, 11, 17, 21, 34, 67, 78, 99}, 55)]
        public void FindPairWithSum_Sorted_2Cursors_HighLowCursorMeetInMiddle(int[] nums, int sum)
        {
            var pair = Program.FindPairWithSum_Sorted_HighLowCursorMeetInMiddle(nums, sum);
            
            Debug.WriteLine(pair.ToString());
        }


        [Theory]
        [InlineData(new [] {4, 9, 11, 17, 21, 34, 67, 78, 99}, 55)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 2)]
        public void FindPairWithSum_Sorted_BinarySearch_SumMinusCurrentNumGetDifference_FindDifferenceInArray_Recusion(int[] nums, int sum)
        {
            var pair = Program.FindPairSum_Sorted_By_BinarySearch_RecusionVersion(nums, sum);

            Trace.WriteLine(pair.ToString());
        }

        [Theory]
        [InlineData(new [] {4, 9, 11, 17, 21, 34, 67, 78, 99}, 55)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 2)]
        public void FindPairWithSum_Sorted_BinarySearch_SumMinusCurrentNumGetDifference_FindDifferenceInArray_WhileLoop(int[] nums, int sum)
        {
            var pair = Program.FindPairSum_Sorted_By_BinarySearch_WhileLoopVersion(nums, sum);

            Trace.WriteLine(pair.ToString());
        }

        [Theory]
        [InlineData(new [] {4, 9, 11, 17, 21, 34, 67, 78, 99}, 55)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 2)]
        public void FindPairWithSum_UnSorted_LinearLoop_StoreCompliments(int[] nums, int sum)
        {
            var pair = Program.FindPairWithSum_Unsorted_LinearLoop_StoreCompliments(nums, sum);

            Trace.WriteLine(pair.ToString());
        }
    }