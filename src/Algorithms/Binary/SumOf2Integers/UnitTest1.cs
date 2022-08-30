namespace SumOf2Integers;

public class UnitTest1
{
    //Given two integers a and b, return the sum of the two integers without using the operators + and -.

    [Fact]
    public void Test1()
    {

        var s = new Solution();
        int result = s.GetSum(13, 3);
        Console.WriteLine($"{result} - {Convert.ToString(result, 2)}");
    }

    public class Solution {
    public int GetSum(int a, int b) {
        
        int carry = a & b; //find anything to carry forward
        int result = a ^ b;

        while (carry != 0) {

            int shiftedCarry = carry << 1;  //left shift to carry 1 forward
            carry = result  & shiftedCarry; // check if result and shifted still has any carrys
            result = result ^ shiftedCarry;

        }

        return result;

    }
}
}