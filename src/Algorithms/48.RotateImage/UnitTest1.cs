namespace _48.RotateImage;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        int[][] matrix = new int[3][];

        matrix[0] = new int[] {1,2,3};
        matrix[1] = new int[] {4,5,6};
        matrix[2] = new int[] {7,8,9};
        // {7,4,1},
        // {8,5,2},
        // {9,6,3},

        var s = new Solution();
        //s.Rotate(matrix);

        s.TransposeRowColumnColumnRow(matrix);
        s.Reverse(matrix);

    }
}

public class Solution {

    private List<Tuple<int,int>> _swapped = new List<Tuple<int,int>>();

    public void Rotate(int[][] matrix) {
        
        for(int row = 0; row < matrix.Length; row ++)
        {
            for(int col = 0; col < matrix.Length; col ++)
            {
                int currentNo = matrix[row][col];

                //to rotate, row becomes column
                //column becomes row

                int toSwapCol = matrix.Length - (row + 1);
                int toSwapRow = col;
                int tempToSwap = matrix[toSwapRow][toSwapCol]; 

                
                if(_swapped.Contains(new Tuple<int, int>(row, col)))
                    continue;

                //do the swap
                matrix[toSwapRow][toSwapCol] = currentNo;

                matrix[row][col] = tempToSwap;

                _swapped.Add(new Tuple<int, int>(toSwapRow, toSwapCol));
            }
        
        }
    }

    public void TransposeRowColumnColumnRow(int[][] matrix)
    {
        for(int row = 0; row < matrix.Length; row ++)
        {
            for(int col = row; col < matrix.Length; col ++)
            {
                int currentNo = matrix[row][col];
                int transposeTarget = matrix[col][row];

                matrix[row][col] =transposeTarget;

                matrix[col][row] = currentNo;
            }
        }
    }

    public void Reverse(int[][] matrix)
    {
        int columnUpperBound = matrix.Length / 2;

        for(int row = 0; row < matrix.Length; row ++)
        {
            for(int col = 0; col < columnUpperBound; col ++)
            {
                int currentNo = matrix[row][col];

                int reverseTargetCol = (matrix.Length -1) - col;
                int reverseTarget = matrix[row][reverseTargetCol];

                matrix[row][col] = reverseTarget;

                matrix[row][reverseTargetCol] = currentNo;
            }
        }
    }
    
}