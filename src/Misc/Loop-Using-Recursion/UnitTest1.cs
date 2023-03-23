namespace Loop_Using_Recursion;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        
        //test recursion in loop

        var t = new TestRecursionInLoop();
        t.Rec(3);

        //problem
        // write a function Loop(st`art_at_num, end_at_num, step)

        var s = new Solution();
        //var r1 = s.Loop(1, 4, 1); // 1, 2, 3
        var r2 = s.Loop(-2, 5, 2); // -2, 0, 2, 4

        //Console.WriteLine(String.Join(",", r1));
        Console.WriteLine(String.Join(",", r2));
    }
}


public class Solution
{
    public int[] Loop(int startNum, int endNum, int step)
    {
        var result = new List<int>();
        LoopRecursive(startNum, endNum, step, result);
        return result.ToArray();
    }

    private int[] LoopRecursive(int startNum, int endNum, int step,List<int> result)
    {
        //base case
        if (startNum >= endNum) {
            return result.ToArray();
        }

        result.Add(startNum);
        

        //recursive case
        return LoopRecursive(startNum + step, endNum, step, result );
    }
}

public class TestRecursionInLoop {

    public void Rec(int x){ 
        Console.WriteLine($"new function, x = {x}");
        for(int i=0; i<x; ++i) {
            Console.WriteLine($"i = {i}, x = {x}");
            Rec(i); 
        }
            
            // STOP 
    } 
}
