using System.Security.Cryptography;
using System.Text;

namespace SpontaneousTest;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {

        var mystring1 = "daa2312dsdssa";
        int i = HashStrToNumber(mystring1);
        var mystring2 = "daa2312dsdssav";
        i = HashStrToNumber(mystring2);
        var mystring3 = "daa2312dsdssa";
        i = HashStrToNumber(mystring3);

        
        // MD5 md5Hasher = MD5.Create();
        // var hashed = md5Hasher.ComputeHash(Encoding.UTF8.GetBytes(mystring));
        // var ivalue = BitConverter.ToInt32(hashed, 0);

        int theBase = 3;
        // int r = Exponetial(theBase, 8, theBase);
        // Assert.True(r == 6561);

        int r2 = ExponetialDivideConquer(theBase, 8);
    }

    private int HashStrToNumber(string s)
    {
        MD5 md5Hasher = MD5.Create();
        var hashed = md5Hasher.ComputeHash(Encoding.UTF8.GetBytes(s));
        var ivalue = BitConverter.ToInt32(hashed, 0);
        return ivalue;
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