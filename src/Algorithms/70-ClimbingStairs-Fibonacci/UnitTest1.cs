using System.Collections;

namespace _70_ClimbingStairs_Fibonacci;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var solution = new Solution();
        int result = solution.ClimbStairs(4);
        Console.WriteLine(result.ToString());
    }
}

public class Solution {
    public int ClimbStairs(int n) {
        
        Hashtable memo = new Hashtable();
        int result =  ClimbStairsBottomWithXSteps(4, new int[]{1,3,5}); //ClimbStairsBottomUp(4); //ClimbStairsMemoize(n,memo);
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

    private int ClimbStairsBottomUp(int n)
    {
        if( n == 1)
            return 1;
        if(n ==2)
            return 2;


        Hashtable nums = new Hashtable();
        nums[0] = 1;
        nums[1] = 1;

        for(int i = 2; i <= n; i ++)
        {
            nums[i] = (int)nums[i - 1] + (int)nums[i - 2];
        }

        return (int)nums[n];
    }

    // x = [1,3,5]
    private int ClimbStairsBottomWithXSteps(int n, int[] xSteps)
    {
        if(n == 0)
            return 1;
        if(n == 1)
            return 1;

        var stepWaysTracker = new Hashtable();

        stepWaysTracker[0] = 1;
        stepWaysTracker[1] = 1;

        for(int i = 2; i <= n; i++)
        {
            int total = 0;
            foreach(int x in xSteps)
            {
                if (i - x >= 0)
                    total += (int)stepWaysTracker[i - x];
            }

            stepWaysTracker[i] = total;
        }

        return (int)stepWaysTracker[n];
    }
}