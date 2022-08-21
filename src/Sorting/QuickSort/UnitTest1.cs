namespace QuickSort;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {

        

        // var swap = (int[,] array, int s, int e) => {
        //     int temp = array[s,];
        // };

        // int[] numbers = CreateRandomArray(10);

        // var qs = new QuickSorter();

        // Console.WriteLine(string.Join(", ", numbers));

        // qs.Sort(numbers);

        // Console.WriteLine(string.Join(", ", numbers));

    }

    private int[] CreateRandomArray(int noOfElements) 
    {
        var rand = new Random();
        var result = new List<int>();

        foreach(int x in Enumerable.Range(0, noOfElements)) {
            result.Add(rand.Next(1, 100));
        }

        return result.ToArray();
    }
}

public class QuickSorter
{
    public void Sort(int[] numbers)
    {
        Sort(numbers, 0, numbers.Length - 1);
    }

    public void Sort(int[] numbers, int leftPointerIndex = 0, int rightPointerIndex = 0)
    {
        int lastArrayIndex = numbers.Length - 1;

        if(leftPointerIndex >= rightPointerIndex) //when sub array only has 1 item to evaluate, return
            return;

        //this is important. The pivot is determine using the passed in left and right pointer index.
        //This make sure pivot falls only with "new" sub-array determine by left and right pointers
        int pivotIndex = (leftPointerIndex +  rightPointerIndex ) / 2;
        int pivot = numbers[pivotIndex]; //pivot selected is last element

        int lastLeftPointerIndexWhereItStops = Partition(numbers, leftPointerIndex, rightPointerIndex, pivot);

        Sort(numbers, leftPointerIndex, lastLeftPointerIndexWhereItStops - 1);

        Sort(numbers, lastLeftPointerIndexWhereItStops, rightPointerIndex);        
    }

    private int Partition(int[] numbers, int leftPointer, int rightPointer, int pivotValue)
    {
        while(leftPointer <= rightPointer) {

            // find finders that are larger than pivor value and left an droght pointer have not meet in the "middle"
            //breaks loop when a larger-tahn pivot value is found
            while(numbers[leftPointer] < pivotValue ) {
                leftPointer++;
            }

            //breaks loop when smaller-than pivot value is found
            while(numbers[rightPointer] > pivotValue ) {
                rightPointer--;
            }

            //once left and right pointer stops, begin to swap
            if(leftPointer <= rightPointer) {
                SwapArrayItem(numbers, leftPointer, rightPointer);

                //after swapping move both pointers 1 items "inwards"
                leftPointer++;
                rightPointer--;
            }
        }
        
        //return the left pointer index, so that subsequent recursion knows the start and end of left-subarray and right-subarray
        return leftPointer;
    }

    private void SwapArrayItem(int[] numbers, int index1, int index2) {

        int temp = numbers[index1];

        numbers[index1] = numbers[index2];

        numbers[index2] = temp;
    }
}