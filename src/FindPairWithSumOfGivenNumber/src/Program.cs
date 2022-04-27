using System;

namespace FindPairWithSumOfGivenNumber
{
    public class Program
    {
        static void Main(string[] args)
        {
            var nums = new [] {1, 3, 4, 7, 18};
            int sum = 19;
            var result = FindPairSum_Sorted_By_BinarySearch_LogN(nums, sum);
            Console.WriteLine(result.ToString());
        }

        public static Tuple<int, int> FindPairWithSumInArray_Sorted(int[] nums, int sum)
        {
            int low = 0;
            int high = nums.Length - 1;

            //while low/high cursor dont meet, loop still runs
            while (low != high) 
            {
                int result = nums[low] + nums[high];

                if (result == sum)
                    return new Tuple<int, int>(nums[low], nums[high]);

                if (result > sum) {
                    high--;
                    continue;
                }

                if (result < sum) {
                    low++;
                    continue;
                }

            }

            return new Tuple<int, int>(-1, -1);
        }

        public static Tuple<int, int> FindPairSum_Sorted_By_BinarySearch_LogN(int[] nums, int sum)
        {
             

             for(int i = 0; i < nums.Length; i++)
             {
                 int currentNumber = nums[i];
                 int difference = sum - currentNumber;

                 int searchResult = BinarySearchWhileLoop(nums, difference);

                 if(searchResult != -1) {
                     return new Tuple<int, int>(currentNumber, searchResult);
                 }
             }

             return new Tuple<int, int>(-1, -1);
        }

        private static int BinarySearchWhileLoop(int[] nums, int itemToFind)
        {

                 int lowIndex = 0;
                 int highIndex = nums.Length -1;

                 while( lowIndex <= highIndex )
                {
                    int midIndex = GetAverage(lowIndex, highIndex);
                    int guess = nums[midIndex];

                    int low = nums[lowIndex];
                    int high = nums[highIndex];

                    if (guess == itemToFind)
                        return guess;

                    if (guess > itemToFind) {
                        highIndex = midIndex - 1;
                        continue;
                    }

                    if (guess < itemToFind) {
                        lowIndex = midIndex + 1;
                        continue;
                    }
                } 
            return -1;
        }

        private static int BinarySearchRecusion(int[] nums, int itemToFind)
        {
            int lowKey = 0;
            int highKey = nums.Length - 1;

            int midKey = GetAverage(lowKey, highKey);

            int myGuess = nums[midKey];

            return -1;
        }

        

        private static int GetAverage(int num1, int num2)
        {
            return Convert.ToInt32( Math.Floor( Convert.ToDecimal( (num2 + num1) / 2)));
        }

        public static Tuple<int, int> FindPairWithSumInArray_Unsorted_By_Number_Difference_Stored_Separately(int[] nums, int sum)
        {
             return new Tuple<int, int>(-1, -1);
        }
    }
}
