namespace SelectionSort_27_03_2023;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        //https://www.youtube.com/watch?v=cqh8nQwuKNE

        var s = new Solution();

        var sorted = s.SelectionSort(new int[] { 11, 3, 44, 88, 34, 22, 12});

        Console.WriteLine(string.Join(", ", sorted));
    }
}

public class Solution
{
    int minValue = 0;
    int minIndex = 0;
    int tempVal = 0;

    //Seletion sort is an inplace sorrting technique
    //in-place meaning
    public int[] SelectionSort(int[] nums)
    {
        for(int i = 0; i < nums.Length; i++)
        {
            minValue = nums[i];
            minIndex = i;

            for(int j = i + 1; j < nums.Length; j++)
            {
                //find smaller value store its index
                if(nums[j] < minValue) {
                    minValue = nums[j];
                    minIndex = j;
                }
            }

            //swap 
            if (minValue < nums[i]) {
                tempVal = nums[i];
                nums[i] = nums[minIndex];
                nums[minIndex] = tempVal;
            }
        }

        return nums;
    }
}