namespace MergeSort;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int[] randomNums = CreateArrayRandomNumbers();

        Console.WriteLine($"numbers: {string.Join(", ", randomNums)}");

        var mergeSorter = new MergeSorter();

        int[] sorted = mergeSorter.MergeSort(randomNums);
    }

    private int[] CreateArrayRandomNumbers()
    {
        var rand = new Random();
        var randList = new List<int>();

        foreach(int x in Enumerable.Range(0, 11)) {

            randList.Add(rand.Next(1, 100));
        }

        return randList.ToArray();
    }
}

public class MergeSorter
{
    public int[] MergeSort(int[] numbers)
    {
        int arrLength = numbers.Length;

        if (arrLength < 2) // just 1 element
            return numbers;

        int sliceStartIndex = 0;
        int midIndex = GetMiddleIndex(numbers);

        int[] left = numbers.Take(new Range(sliceStartIndex, midIndex)).ToArray(); // first to mid

        int[] right = numbers.Take(new Range(midIndex, numbers.Length)).ToArray(); // mid to end

        Console.WriteLine($"Left: {string.Join(", ", left)}");
        Console.WriteLine($"Right: {string.Join(", ", right)}");

        //recurse to further split left and right
        MergeSort(left);

        MergeSort(right);

        

        // length of left + right = originalNumbers length
        //MergeLeftRight(numbers, left, right); // when first calling this method, left and right only have 1 element each
        MergeLeftRight_WithLinq(numbers, left, right);

        return numbers;
    }

    // length of left + right = originalNumbers length
    public void MergeLeftRight(int[] originalNumbers, int[] left, int[] right)
    {
        var mergedUnsorted = left.Concat(right);

        int leftIndex = 0, rightIndex = 0, originalIndex = 0;

        while(leftIndex < left.Length && rightIndex < right.Length) {

            int leftVal = left[leftIndex];

            int rightVal = right[rightIndex];

            if (rightVal <= leftVal) {
                originalNumbers[originalIndex] = rightVal;
                rightIndex++; // right array move to next item to compare left "same" item 
                originalIndex++;
            }
            else {
                originalNumbers[originalIndex] = leftVal;
                leftIndex++; // left array move to next item to compare right "same" item 
                originalIndex++;
            }
        }

        //merge leftover elements from left array
        //leftIndex stop incrementing from previous while loop, start from where leftIndex stopped at
        if(leftIndex < left.Length) {
            while(leftIndex < left.Length) {
                int leftVal = left[leftIndex];
                originalNumbers[originalIndex] =leftVal;
                leftIndex++;
                originalIndex++;
            }
        }

        if(rightIndex < right.Length) {
            while(rightIndex < right.Length) {
                int rightVal = right[rightIndex];
                originalNumbers[originalIndex] =rightVal;
                rightIndex++;
                originalIndex++;
            }
        }
    }

    private void MergeLeftRight_WithLinq(int[] originalNumbers, int[] left, int[] right)
    {
        var merged = new List<int>();
        merged.AddRange(left);
        merged.AddRange(right);

        var sorted = merged.OrderBy(x => x);

        int[] sortedArray = sorted.ToArray();

        for(int i = 0; i < originalNumbers.Length; i++) {
            int val = sortedArray[i];
            originalNumbers[i] = val;
        }
    }

    private int GetMiddleIndex(int[] numbers)
    {
        int arrLength = numbers.Length;

        if(arrLength % 2 == 0) {
            return arrLength / 2;
        }
        else {
            int mid = arrLength / 2;
            return mid + 1;
        }
    }

}