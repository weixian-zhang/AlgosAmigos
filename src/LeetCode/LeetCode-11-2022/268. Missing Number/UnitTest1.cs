namespace MissingNumber;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int a = 2;
        int b = 3;

        int or = a | b;
        int ors = a | a;

        int xor = a ^ b;
        int xors = a ^ a;

        int and = a & b;
        int ands = a & a;

        var s = new Solution();
        int missing = s.MissingNumber(new int[] {6,4,2,3,5,7,0,9,8});
    }

    public class Solution {
        public int MissingNumber(int[] nums) {
            
            int max = nums.Length;

            for(int i=0; i <= max; i++)
            {
                if(nums.Where(x => x == i).Count() == 0)
                    return i;
            }

            return 0;
            
        }
    }
}