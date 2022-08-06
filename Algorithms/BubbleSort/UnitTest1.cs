namespace BubbleSort;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int[] array = {10, 77, 5, 100, 78, 66, 44};

        var bs=new BubbleSorter();

        var sorted = bs.Sort(array);
    }

    public class BubbleSorter
    {
        public int[] Sort(int[] numbers)
        {
            for(int i = 0; i < numbers.Length; i++)
            {
                for(int j = i + 1; j < numbers.Length; j++)
                {
                    int left = numbers[i];
                    int right = numbers[j];

                    if (left > right)
                    {
                        int leftTemp = numbers[i];
                        numbers[i] = right;
                        numbers[j] = leftTemp;
                    }
                }
                
            }

            return numbers;
        }
    }
}