namespace BinarySearch;

public class UnitTest1
{
    [Fact]
    public void Test_BinarySearch_Number_Exist()
    {
        int[] numbers = {3, 6, 11, 52, 100, 210};

        int result1 = BinarySearchNumber(numbers, 6);


        Assert.True(result1 == 6);
        
    }

    [Fact]
    public void Test_BinarySearch_Number_Not_Exist()
    {
        int[] numbers = {3, 6, 11, 52, 100, 210};

        int result2 = BinarySearchNumber(numbers, 255);

        Assert.True(result2 == -1);
    }

    [Fact]
    public void Test_BinarySearch_Number_Text_Exist()
    {
        string[] texts = {"abercrombie", "dough", "moses", "nash", "yakshaa", "zee"};

        bool found1 = BinarySearchText(texts, "zoo");

        bool found2 = BinarySearchText(texts, "zee");
        
        Assert.True(found1 == false);

        Assert.True(found2 == true);
    }

    private int BinarySearchNumber(int[] numbers, int numToSearch)
    {
        return BSNumber(numbers, numToSearch, 0, numbers.Length - 1);
    }

    public int BSNumber(int[] numbers, int numToSearch, int left, int right)
    {
        if (left > right) //cannot find
            return -1;


        int mid = (left + right) / 2;

        int midValue = numbers[mid];

        if (numToSearch == midValue)
            return midValue;

        if (numToSearch > midValue) {
            left = mid + 1;
        }

        if(numToSearch < midValue) {
            right = mid - 1;
        }

        return BSNumber(numbers, numToSearch, left, right);

    }

    private bool BinarySearchText(string[] texts, string toSearch)
    {
        return BSSearchText( texts, toSearch, 0, texts.Length - 1);
    }

    private bool BSSearchText(string[] texts, string toSearch, int left, int right)
    {
        if (left > right)
            return false;

        int midIndex = (left + right) / 2;

        string midValue = texts[midIndex];

        if (toSearch == midValue)
            return true;

        // the = is needed because same char e.g Z > Z will not meet this condition.
        //causes recursion to have no base case, forever recurse

        if ((int)toSearch[0] >= (int)midValue[0]) { 
            left = midIndex + 1;
        }

        if ((int)toSearch[0] <= (int)midValue[0]) {
            right = midIndex - 1;
        }

        return BSSearchText(texts, toSearch, left, right);
    }
}