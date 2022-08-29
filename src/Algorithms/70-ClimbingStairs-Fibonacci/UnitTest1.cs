using System.Collections;

namespace _70_ClimbingStairs_Fibonacci;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var solution = new Solution();
        int result = solution.ClimbStairs(5);
        Console.WriteLine(result.ToString());
    }
}

public class Solution {
    public int ClimbStairs(int n) {
        
        Hashtable memo = new Hashtable();
        int result = ClimbStairsMemoize(n,memo);
        return result;
    }
    
    private int ClimbStairsMemoize(int n, Hashtable memo) {
        //base case
        if(n == 1)
            return 1;
        if(n == 2)
            return 2;
        
        if(memo.ContainsKey(n))
            return (int)memo[n];
        
        int n1 = ClimbStairsMemoize(n - 1, memo);
        int n2 = ClimbStairsMemoize(n - 2, memo);
        int result = n1 + n2;

        Console.WriteLine($"{result} = {n1} + {n2}");

        memo[n] = result;
        
        
        
        return result;
    }
}