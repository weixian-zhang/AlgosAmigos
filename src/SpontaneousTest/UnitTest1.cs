namespace SpontaneousTest;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int theBase = 3;
        // int r = Exponetial(theBase, 8, theBase);
        // Assert.True(r == 6561);

        int r2 = ExponetialDivideConquer(theBase, 8);
    }

    public int Exponetial(int baseOf, int n, int result)
    {
        if(n == 1)
            return baseOf;

        result *= Exponetial(baseOf, n-1, result);

        return result;
    }

    public int ExponetialDivideConquer(int baseOf, int power)
    {
        if(power == 0)
            return 1;

        int halfPower = ExponetialDivideConquer(baseOf, power / 2);
        int fullPower = halfPower * halfPower;
        if(power % 2 == 1) //odd number
        {
            fullPower = fullPower * baseOf;
        }

        return fullPower;
    }
}