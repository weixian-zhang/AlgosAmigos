using Xunit;
using BFSN;

namespace test;


public class TestBFS
{
    public TestBFS()
    {
        
    } 

    [Fact]
    public void Test_Search()
    {
        var graph = new Dictionary<int, List<int>>(){
            {0, new List<int>() {1,2} },
            {1, new List<int>() {0,2,3} },
            {2, new List<int>() {0,1,4} },
            {3, new List<int>() {1,4} },
            {4, new List<int>() {2, 3} },
        };

        var bfs = new BFS();

        //int[] route = bfs.Search(graph, 0);


        //Console.WriteLine(string.Join(",", route));

        
    }
}