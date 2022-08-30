namespace NumberOfOneBits;


//Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

// Input: n = 00000000000000000000000000001011
// Output: 3
// Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

public class UnitTest1
{
    [Fact]
    public void Test1()
    {

        var s = new Solution();
        int noOfOnes = s.HammingWeight(00000000000000000000000000001011);

        Assert.True(noOfOnes == 3);
    }

    public class Solution {
        public int HammingWeight(uint n) {
            
            string bits = Convert.ToString(n);
            int r = bits.Where(x => x.ToString() == "1").Count();        
            return r;    
        }
    }
}