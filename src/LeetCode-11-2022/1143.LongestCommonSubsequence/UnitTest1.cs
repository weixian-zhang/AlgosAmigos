namespace _1143.LongestCommonSubsequence;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        string text1 = "abcde";
        string text2 = "ace";

        var s = new Solution();
        int r = s.LongestCommonSubsequence(text1, text2);
    }
}

public class Solution {
    public int LongestCommonSubsequence(string text1, string text2) {
        
        int text1Length = text1.Length + 1;
        int text2Length = text2.Length + 1;

        int[][] dp = CreateDPArray(text1Length, text2Length);

        for (int i = 0; i < text1.Length; i++)
        {
           for (int j = 0; j < text2.Length; j++)
            {
                //match the indexes of dp matrix with empty string first row/col
                int currentI = i + 1;
                int currentJ = j + 1;

                //carry value from "above"
                int valueAbove = dp[currentI - 1][currentJ];
                dp[currentI][currentJ] = valueAbove;

                if(text1[i] == text2[j])
                {
                    //1 + diagnonal up+left cell value
                    int currentCharMatchCell =  dp[i+1][j+1];

                    //if i,j is not 0, then -1 to get previous up+left diagonal row
                    int diagonalUpI = currentI - 1;
                    int diagonalUpJ = currentJ - 1;
                    int diagonalUpPrevCellVal = dp[diagonalUpI][diagonalUpJ];

                    dp[currentI][currentJ] = 1 + diagonalUpPrevCellVal;
                }
                else
                {
                    //ignore if col = 1 which is 1 col after empty string
                    //this cell value is brought down from previous row
                    if(currentJ == 1)
                        continue;

                    int prevJ = currentJ - 1;

                    int prevCellValue = dp[currentI][currentJ - 1];

                    //previous value carry to current cell
                    dp[currentI][currentJ]  = Math.Max(prevCellValue, valueAbove);
                }
            } 
        }

        int result = dp[text1Length -1][text2Length-1];

        return result;

    }

    private int[][] CreateDPArray(int length1, int length2)
    {
        int[][] dp = new int[length1][]; //+1 to handle blank string

        for (int i = 0; i < length1; i++)
        {
           for (int j = 0; j < length2; j++)
            {
                if(dp[i]  == null)
                    dp[i] = new int[length2];

                dp[i][j] = 0;
            } 
        }

        return dp;
    }
}