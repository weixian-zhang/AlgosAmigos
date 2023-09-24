namespace _36.ValidSudoku;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        // char[][] board = new char[][]
        // {
        //     // new char[] {'5','3','.','.','7','.','.','.','.'},
        //     // new char[] {'6','.','.','1','9','5','.','.','.'},
        //     // new char[] {'.','9','8','.','.','.','.','6','.'},
        //     // new char[] {'8','.','.','.','6','.','.','.','3'},
        //     // new char[] {'4','.','.','8','.','3','.','.','1'},
        //     // new char[] {'7','.','.','.','2','.','.','.','6'},
        //     // new char[] {'.','6','.','.','.','.','2','8','.'},
        //     // new char[] {'.','.','.','4','1','9','.','.','5'},
        //     // new char[] {'.','.','.','.','8','.','.','7','9'},
        // };

        char[][] board = new char[][]
        {
            new char[] {'.','.','.','.','5','.','.','1','.'},
            new char[] {'.','4','.','3','.','.','.','.','.'},
            new char[] {'.','.','.','.','.','3','.','.','1'},
            new char[] {'8','.','.','.','.','.','.','2','.'},
            new char[] {'.','.','2','.','7','.','.','.','.'},
            new char[] {'.','1','5','.','.','.','.','.','.'},
            new char[] {'.','.','.','.','.','2','.','.','.'},
            new char[] {'.','2','.','9','.','.','.','.','.'},
            new char[] {'.','.','4','.','.','.','.','.','.'}
        };

        var s = new Solution();

        bool result = s.IsValidSudoku(board);
    }
}

public class Solution {
    public bool IsValidSudoku(char[][] board) {
        
        char[][] _3x3_1 = new char[3][];
        char[][] _3x3_2 = new char[3][];
        char[][] _3x3_3 = new char[3][];
        char[][] _3x3_4 = new char[3][];
        char[][] _3x3_5 = new char[3][];
        char[][] _3x3_6 = new char[3][];
        char[][] _3x3_7 = new char[3][];
        char[][] _3x3_8 = new char[3][];
        char[][] _3x3_9 = new char[3][];

        var charList = new List<char>();

        HashSet<char> hashset = null;

        for(int row = 0; row <= 8; row++)
        {
            hashset = new HashSet<char>();

            for(int col = 0; col <= 8; col++)
            {
                char cellVal = board[row][col];

                if(cellVal != '.')
                    if(!hashset.Contains(cellVal))
                        hashset.Add(cellVal);
                    else
                        return false;
                //1
                if(row >= 0 && row <= 2 && col >= 0 && col <= 2)
                {
                   if(_3x3_1[row] == null)
                        _3x3_1[row] = new char[3];

                    _3x3_1[row][col] = cellVal;
                }

                //2
                if(row >= 0 && row <= 2 && col >= 3 && col <= 5)
                {
                    int _3x3Col = col - 3;

                    if(_3x3_2[row] == null)
                        _3x3_2[row] = new char[3];

                    _3x3_2[row][_3x3Col] = cellVal;
                }

                //3 
                if(row >= 0 && row <= 2 && col >= 6 && col <= 8)
                {
                   int _3x3Col = col - 6;

                    if(_3x3_3[row] == null)
                        _3x3_3[row] = new char[3];

                    _3x3_3[row][_3x3Col] =cellVal;
                }

                //4
                if(row >= 3 && row <= 5 && col >= 0 && col <= 2)
                {
                   int _3x3Row = row - 3;

                   if(_3x3_4[_3x3Row] == null)
                        _3x3_4[_3x3Row] = new char[3];

                    _3x3_4[_3x3Row][col] =cellVal;
                }

                //5
                if(row >= 3 && row <= 5 && col >= 3 && col <= 5)
                {
                    int _3x3Row = row - 3;
                   int _3x3Col = col - 3;

                    if(_3x3_5[_3x3Row] == null)
                        _3x3_5[_3x3Row] = new char[3];

                    _3x3_5[_3x3Row][_3x3Col] =cellVal;
                }

                //6
                if(row >= 3 && row <= 5 && col >= 6 && col <= 8)
                {
                    int _3x3Row = row - 3;
                   int _3x3Col = col - 6;

                    if(_3x3_6[_3x3Row] == null)
                        _3x3_6[_3x3Row] = new char[3];

                    _3x3_6[_3x3Row][_3x3Col] =cellVal;
                }

                //7
                if(row >= 6 && row <= 8 && col >= 0 && col <= 2)
                {
                    int _3x3Row = row - 6;

                    if(_3x3_7[_3x3Row] == null)
                        _3x3_7[_3x3Row] = new char[3];

                    _3x3_7[_3x3Row][col] =cellVal;
                }

                //8
                if(row >= 6 && row <= 8 && col >= 3 && col <= 5)
                {
                    int _3x3Row = row - 6;
                   int _3x3Col = col - 3;

                    if(_3x3_8[_3x3Row] == null)
                        _3x3_8[_3x3Row] = new char[3];

                    _3x3_8[_3x3Row][_3x3Col] =cellVal;
                }

                //9
                if(row >= 6 && row <= 8 && col >= 6 && col <= 8)
                {
                    int _3x3Row = row - 6;
                   int _3x3Col = col - 6;

                    if(_3x3_9[_3x3Row] == null)
                        _3x3_9[_3x3Row] = new char[3];

                    _3x3_9[_3x3Row][_3x3Col] =cellVal;
                }
                
            }
        }

        if(Is3x3CellsValid(_3x3_1) && Is3x3CellsValid(_3x3_2) && Is3x3CellsValid(_3x3_3) &&
            Is3x3CellsValid(_3x3_4) && Is3x3CellsValid(_3x3_5) && Is3x3CellsValid(_3x3_6) &&
            Is3x3CellsValid(_3x3_7) && Is3x3CellsValid(_3x3_8) && Is3x3CellsValid(_3x3_9) && Is9x9ColumnWiseValid(board))
            {
                return true;
            }

        return false;
    }

    private bool Is9x9ColumnWiseValid(char[][] board)
    {
        HashSet<char> hashset = null;

        for (int col = 0; col < 9; col++)
        {
            hashset = new HashSet<char>();

            for (int row = 0; row < 9; row++)
            {
                char cellVal = board[row][col];

                if(cellVal != '.')
                    if(!hashset.Contains(cellVal))
                        hashset.Add(cellVal);
                    else
                        return false;
            }
        }

        return true;
    }

    private bool Is3x3CellsValid(char[][] cells)
    {
        var numbers = new HashSet<char>();

        for(int row = 0; row <= 2; row++)
        {
            for(int col = 0; col <= 2; col++)
            {
                char c = cells[row][col];

                if(c != '.')
                {
                    if(!numbers.Contains(c))
                        numbers.Add(c);
                    else
                        return false;
                }
            }
        }

        return true;
    }
}