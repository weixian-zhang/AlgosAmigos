namespace SelectionSort;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int[] array = {10, 77, 5, 100, 78, 3, 66, 44,1,2};

        var bs=new SelectionSorter();

        var sorted = bs.Sort(array);

        Console.WriteLine(string.Join(", ", sorted));
    }

    public class SelectionSorter
    {
        public int[] Sort(int[] numbers)
        {
            int lowestIndex = 0;
            int lowestValue = 0;

            for(int i = 0; i < numbers.Length; i++) {

                lowestValue = numbers[i];
                lowestIndex = i;

                for (int j = i + 1; j < numbers.Length; j++) { //find the smallest num and record the index

                    int nextSmallestItem = numbers[j];

                    if (nextSmallestItem < lowestValue) {
                        lowestValue = nextSmallestItem;
                        lowestIndex = j;
                    }
                }

                //do a swap
                int temp = numbers[i]; //current item

                numbers[i] = numbers[lowestIndex];

                numbers[lowestIndex] = temp;

            }

            return  numbers;
        }
    }
}