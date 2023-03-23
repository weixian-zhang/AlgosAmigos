namespace DFS_23032023;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new Dictionary<int, List<int>>();
        g[0] = new List<int>() { 1, 2};
        g[1] = new List<int>() { 0, 3};
        g[2] = new List<int>() { 0, 3};
        g[3] = new List<int>() { 1, 4, 2};
        g[4] = new List<int>() { 3};

        var s = new Solution();
        var paths = s.DFS(g);

        Console.WriteLine(String.Join(",", paths));
    }
}

public class Solution
{
    public List<int> DFS(Dictionary<int, List<int>> graph) 
    {
        var result = new List<int>();
        var hashset = new HashSet<int>();

       var paths = DFSRecursive(0, graph, hashset, result);

        return result;
    }

    private List<int> DFSRecursive(int nodeToTraverse, Dictionary<int, List<int>> graph, HashSet<int> visitedNodes, List<int> resultPath) 
    {
        //base case - when all nodes has finished traversal

        if(visitedNodes.Contains(nodeToTraverse)) {
            return resultPath;
        }

        if ( visitedNodes.Count == graph.Count) {
            return resultPath;
        }

        visitedNodes.Add(nodeToTraverse);

        resultPath.Add(nodeToTraverse);

        var nodes = graph[nodeToTraverse];

        foreach(int n in nodes) {
            DFSRecursive(n, graph, visitedNodes, resultPath);
        }

        return resultPath;
    }
}