using System;
using System.Collections;
using System.Collections.Generic;

namespace FindPairWithSumOfGivenNumber
{
    public class Program
    {
        static void Main(string[] args)
        {
            // var nums = new [] {4, 9, 11, 17, 21, 34, 67, 78, 99};
            // int sum = 55;
            // var result = FindPairSum_Sorted_By_BinarySearch_RecusionVersion(nums, sum);
            // Console.WriteLine(result.ToString());

            var nums = new [] {14, 9, 11, 71, 41, 34, 67, 78, 99, 86, 92, 0};
            int sum = 92;
            var result = FindPairWithSum_Unsorted_LinearLoop_StoreCompliments(nums, sum);
            Console.WriteLine(result.ToString());
        }

        public static Tuple<int, int> FindPairWithSum_Unsorted_LinearLoop_StoreCompliments(int[] nums, int sum)
        {
            var complimentsHistory = new HashSet<int>();

            for(int i =0; i < nums.Length - 1; i++)
            {
                int item = nums[i];

                //move on if first item
                if(i == 0) {
                    int comp = sum - item;

                    complimentsHistory.Add(comp);
                    continue;
                }

                int compliment = sum - item;

                int tryVal = 0;
                if(complimentsHistory.TryGetValue(item, out tryVal)) {
                    int pairingPreviousCompliment = sum - compliment;
                    return new Tuple<int, int>(compliment, pairingPreviousCompliment);
                } else 
                    complimentsHistory.Add(compliment);
            }

            return new Tuple<int, int>(-1, -1);
        }

        public static Tuple<int, int> FindPairWithSum_Sorted_HighLowCursorMeetInMiddle(int[] nums, int sum)
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

        public static Tuple<int, int> FindPairSum_Sorted_By_BinarySearch_RecusionVersion(int[] nums, int sum)
        {
             for(int i = 0; i < nums.Length; i++)
             {
                 int currentNumber = nums[i];
                 int difference = sum - currentNumber;

                 if(difference == 0)
                    continue;

                 //find difference is in array, if any
                 int searchResult = BinarySearchRecusion(nums, 0, 0, difference);

                 if(searchResult != -1) {
                     return new Tuple<int, int>(currentNumber, searchResult);
                 }
             }

             return new Tuple<int, int>(-1, -1);
        }

        public static Tuple<int, int> FindPairSum_Sorted_By_BinarySearch_WhileLoopVersion(int[] nums, int sum)
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

        private static int BinarySearchRecusion(int[] nums, int lowKey, int highKey, int numToFind)
        {
            //first recusion run
            if(lowKey == 0 && highKey == 0) {
                lowKey = 0;
                highKey = nums.Length - 1;
            }

            int midKey = GetAverage(lowKey, highKey);

            int myGuess = nums[midKey];

            //base path
            if (lowKey == highKey)
                return -1;

            //base path
            if (myGuess == numToFind)
                return  myGuess;

            //recurse path
            if (myGuess > numToFind) {
                highKey = midKey - 1;
                return BinarySearchRecusion(nums, lowKey, highKey, numToFind);
            }

            //recurse path
            if (myGuess < numToFind) {
                lowKey = midKey + 1;
                return BinarySearchRecusion(nums, lowKey, highKey, numToFind);
            }

            return -1;
        }

        

        private static int GetAverage(int num1, int num2)
        {
            decimal avg = (num2 + num1) / 2;
            decimal roundDown = Math.Floor(avg);
            int result = Convert.ToInt32(roundDown);

            return result;
        }
    }
}
