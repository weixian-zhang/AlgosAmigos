namespace BoyerMooreMajorityElement;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var numbers = new int[] {1,1,1,1,2,3,5};

        var s = new Solution();

        int majority = s.FindMajority(numbers);
    }
}

public class Solution
{
    public int FindMajority(int[] numbers)
    {
        int candidate = 0;
        int count = 0;

        foreach(int x in numbers)
        {
            if(count == 0) candidate = x;

            if(x == candidate)
                count++;
            else
                count--;
        }
        
        return candidate;
    }
}