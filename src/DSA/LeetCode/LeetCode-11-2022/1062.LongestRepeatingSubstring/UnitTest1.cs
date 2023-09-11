using System.Collections;

namespace _1062.LongestRepeatingSubstring;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        string a = "abbaba";

        var s = new Solution();

        int c = s.LongestRepeatingSubstring(a);
    }
}


public class Solution {

    public int LongestRepeatingSubstring(string s) 
    {
        int strLength = s.Length;

        int[][] dp = CreateDPMatrix(strLength + 1);

        int result = 0;
        
        for (int i = 1; i < dp.Length; i++)
        {
            //start from 2nd char
            for (int j = 1; j < dp.Length; j++)
            {
                int currentI = i;
                int currentJ = j;

                if (s[i-1] == s[j-1] && i != j) //substring cannot compare with 
                {
                    int diagonalUpI = currentI - 1;
                    int diagonalUpJ = currentJ - 1;
                    dp[currentI][currentJ] = dp[diagonalUpI][diagonalUpJ] + 1;

                    result = Math.Max(result, dp[currentI][currentJ]);
                }
                //to get subsequence include following codes
                // else
                // {
                //     int valueOnLeft = dp[currentI][currentJ - 1];
                //     int valueAbove = dp[currentI - 1][currentJ];
                //     dp[currentI][currentJ] = Math.Max(valueOnLeft, valueAbove);
                // }

                // result = dp[currentI][currentJ];
            }
        }
        return result;
    }

    private int[][] CreateDPMatrix(int length)
    {
        int[][] dp = new int[length][];
        for (int i = 0; i < length; i++)
        {
            for (int j = 0; j < length; j++)
            {
                if(dp[i] == null)
                    dp[i] =new int[length];
                dp[i][j] = 0;
            }
        }
        return dp;
    }
}