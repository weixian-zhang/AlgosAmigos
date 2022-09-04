namespace BFS_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new Dictionary<int, List<TreeNode>>();
        g[1] = new List<TreeNode>() {new TreeNode(11), new TreeNode(6)};
        g[11] = new List<TreeNode>() { new TreeNode(1), new TreeNode(10)};
        g[10] = new List<TreeNode>() { new TreeNode(11), new TreeNode(5)};
        g[5] = new List<TreeNode>() { new TreeNode(10), new TreeNode(7),new TreeNode(9) };
        g[6] = new List<TreeNode>() { new TreeNode(9)};
        g[7] = new List<TreeNode>() { new TreeNode(5),new TreeNode(8),};
        g[8] = new List<TreeNode>() { new TreeNode(7),new TreeNode(9) };
        g[9] = new List<TreeNode>() { new TreeNode(5),new TreeNode(6), new TreeNode(8) };

        var s = new Solution();

        var path1 = s.BFS(g, new TreeNode(1), 9);
        var shortestPath = s.FindShortestPath(s.prevNodetracker, 1, 9);
    }
}

public class Solution
{
    Queue<int> _queue = new Queue<int>();
    private List<int> _visited = new List<int>();
    public Dictionary<int, int> prevNodetracker = new Dictionary<int, int>();

    public int[] BFS(Dictionary<int, List<TreeNode>>  graph, TreeNode node, int end)
    {
        _queue.Enqueue(node.Label);


        while(_queue.Count > 0)
        {
            int currentNode = _queue.Dequeue();

            if(!_visited.Contains(currentNode)){
                _visited.Add(currentNode);
            }

            //end node found
            if(currentNode == end)
                break;

            if(graph.ContainsKey(currentNode))
            {
                foreach(var neighbour in graph[currentNode] )
                {
                    if(!_visited.Contains(neighbour.Label))
                    {
                        _queue.Enqueue(neighbour.Label);

                        //track parent node of next node, use to find shortest path later
                        //[neighbour:parent, neighbour:parent, neighbour:parent]
                        prevNodetracker[neighbour.Label] = currentNode;
                    }

                        
                }
            }
        }

        return _visited.ToArray();
    }

    public int[] FindShortestPath(Dictionary<int,int> prevNodetracker, int start, int end)
    {
        var shortestPath = new List<int>();

        shortestPath.Add(end);
        int parent = prevNodetracker[end];

        while(parent != -1)
        {
            shortestPath.Add(parent);

            if(prevNodetracker.ContainsKey(parent))
                parent = prevNodetracker[parent];
            else
                parent = -1;

            //stop as first node of path = specified start
            if(shortestPath[0] == start)
                parent = -1;

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