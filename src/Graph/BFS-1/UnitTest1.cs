namespace BFS_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new Dictionary<int, List<TreeNode>>();
        g[0] = new List<TreeNode>() { new TreeNode(9),new TreeNode(7),new TreeNode(11)};
        g[1] = new List<TreeNode>() {};
        g[2] = new List<TreeNode>() { new TreeNode(12)};
        g[3] = new List<TreeNode>() { new TreeNode(2),new TreeNode(4)};
        g[4] = new List<TreeNode>() { };
        g[5] = new List<TreeNode>() { };
        g[6] = new List<TreeNode>() { new TreeNode(5)};
        g[7] = new List<TreeNode>() { new TreeNode(3),new TreeNode(6)};
        g[8] = new List<TreeNode>() { new TreeNode(1), new TreeNode(12)};
        g[9] = new List<TreeNode>() { new TreeNode(10),new TreeNode(8)};
        g[10] = new List<TreeNode>() { new TreeNode(1)};
        g[11] = new List<TreeNode>() { };
        g[12] = new List<TreeNode>() { };

        var s = new Solution();

        var path1 = s.BFS(g, new TreeNode(0));

        var shortestPath = s.FindShortedPath(path1, 0 ,4);
    }
}

public class Solution
{
    Queue<int> _queue = new Queue<int>();
    private List<int> _visited = new List<int>();
    public int[] BFS(Dictionary<int, List<TreeNode>>  graph, TreeNode node)
    {
        _queue.Enqueue(node.Label);


        while(_queue.Count > 0)
        {
            int currentNode = _queue.Dequeue();

            if(!_visited.Contains(currentNode)){
                _visited.Add(currentNode);
            }
                

            if(graph.ContainsKey(currentNode))
            {
                foreach(var neighbour in graph[currentNode] )
                {
                    if(!_visited.Contains(neighbour.Label))
                        _queue.Enqueue(neighbour.Label);
                }
            }
        }

        return _visited.ToArray();
    }

    public int[] FindShortedPath(int[] bfspath, int start, int end)
    {
        var shortestPath = new List<int>();

        int endOfPath = bfspath.Length - 1;
        
        for(int i = endOfPath; i >= 0; i--)
        {
            if(bfspath[i] == end)
            {
                shortestPath.Add(bfspath[i] );
            }

            if(bfspath[i] == start)
            {
                shortestPath.Add(bfspath[i]);
                break;
            }
        }

        shortestPath.Reverse();

        return shortestPath.ToArray();
    }
}

public class TreeNode
{
    public TreeNode(int label)
    {
        Label = label;
    }
    public int Label { get; set; }
    public int Cost { get; set; }
}