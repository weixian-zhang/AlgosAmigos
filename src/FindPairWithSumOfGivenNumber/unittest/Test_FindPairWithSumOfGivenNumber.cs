using System;
using FindPairWithSumOfGivenNumber;
using Xunit;

public class Test_FindPairWithSumOfGivenNumber
    {
        [Theory]
        [InlineData(new [] {1, 3, 4, 7, 18}, 19)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 32)]
        [InlineData(new [] {4, 9, 11, 17, 21, 34, 67, 78, 99}, 55)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 2)]
        public void Sorted(int[] nums, int sum)
        {
            var pair = Program.FindPairWithSumInArray_Sorted(nums, sum);

            Console.WriteLine(pair.ToString());
        }


        [Theory]
        [InlineData(new [] {1, 3, 4, 7, 18}, 19)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 32)]
        [InlineData(new [] {4, 9, 11, 17, 21, 34, 67, 78, 99}, 55)]
        [InlineData(new [] {4, 9, 11, 17, 21}, 2)]
        public void FindPairSum_Sorted_By_BinarySearch_LogN(int[] nums, int sum)
        {
            var pair = Program.FindPairSum_Sorted_By_BinarySearch_LogN(nums, sum);

            Console.WriteLine(pair.ToString());
        }
    }