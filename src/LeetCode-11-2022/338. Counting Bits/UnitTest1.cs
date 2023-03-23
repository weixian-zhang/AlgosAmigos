namespace CountingBits;

//Given an integer n, return an array ans of length n + 1 such that 
// for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var s = new Solution();
        int bitsToCount = 5;
        Console.WriteLine(string.Join(", ", s.CountBits(bitsToCount)));
    }

    public class Solution {
        public int[] CountBits(int n) {
            
            var result = new List<int>();

            for(int i = 0; i <= n; i++) {

                int r = Convert.ToString(i, 2).Where(b => b.ToString() == "1").Count();
                result.Add(r);
            }

            return result.ToArray();
        
            
        }
    }
}