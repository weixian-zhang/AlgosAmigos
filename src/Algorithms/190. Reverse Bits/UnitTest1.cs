namespace ReverseBits;

//Reverse bits of a given 32 bits unsigned integer.
// Input: n = 00000010100101000001111010011100
// Output:    964176192 (00111001011110000010100101000000)
// Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
// so return 964176192 which its binary representation is 00111001011110000010100101000000.

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();
        uint unsigned = 0b00000010100101000001111010011100;

        s.reverseBits(unsigned);


    }

    public class Solution {
        public uint reverseBits(uint n) {

            var reverseBits = new List<string>();

            string bits = Convert.ToString(n , 2);

            int noOfZeroToPrePad = 32 - bits.Length;

            for(int i = 0; i <= noOfZeroToPrePad - 1; i++) {
                bits = "0" + bits;
            }

            for(int i = bits.Length - 1; i >= 0; i--)
            {
                reverseBits.Add(bits[i].ToString());
            }

            string r = string.Join("", reverseBits);

            uint result = Convert.ToUInt32(r, 2);

            return result;
        }
    }
}