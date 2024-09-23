namespace _498.DiagonalTraverse;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int k = 0;
        int i = k;
        k++;
        k++;

        int[][] mat = new int[][]
        {
            new int[]{1,2,3},
            new int[]{4,5,6},
            new int[]{7,8,9}
        };

        var s = new Solution();
        int[] r = s.FindDiagonalOrder(mat);
    }
}

public class Solution {
    public int[] FindDiagonalOrder(int[][] mat) {

        if(mat.Count() == 0)
            return new int[]{};

        if(mat[0].Count() == 0)
            return new int[]{};

        var result = new List<int>();

        //int noOfDiagonals = GetNumberOfDiagonalTraversals(mat);
        int totalRows = mat.Count();
        int totalCols = mat[0].Count();
        int lastRow = totalRows - 1;
        int lastCol = totalCols - 1;

        int row = 0;
        int col = 0;

        bool UP = true;

        while(row <= lastRow && col <= lastCol)
        {
            if(UP)
            {
                //second row onwards
                while(row > 0 && col < lastCol)
                {
                    result.Add(mat[row][col]);
                    row--;
                    col++;
                }

                result.Add(mat[row][col]);

                if(col == lastCol)
                {
                    row++; //go downwards as last column is reached
                }
                else
                {
                    col++; //continue to go right -->
                }
            }
            //going downwards
            else
            {
                //activate only on 2nd col onwards
                while(row < lastRow && col > 0)
                {
                    result.Add(mat[row][col]);
                    row++;      //going downwards and "left" <--
                    col--;
                }

                result.Add(mat[row][col]);

                if(row == lastRow)
                {
                    col++; //move column right as last row hit
                }
                else
                {
                    row++;
                }
            }

            UP = UP ? false : true; //toggle between true and false
        }
        
        return result.ToArray();
    }

    
}