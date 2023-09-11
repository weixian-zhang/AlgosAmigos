namespace Dijkstra_2;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new Dictionary<string, List<Node>>();
        g["A"] = new List<Node>(){ new Node("B", 3), new Node("C", 1)};
        g["B"] = new List<Node>(){new Node("A", 3),  new Node("C", 7), new Node("D", 5),new Node("E", 1)};
        g["C"] = new List<Node>(){ new Node("B", 7), new Node("D", 2)};
        g["D"] = new List<Node>(){ new Node("C", 2), new Node("B", 5), new Node("E", 7)};
        g["E"] = new List<Node>(){ new Node("B", 1), new Node("D", 7)};

        var s = new Solution();

        int shortestCost= s.DijkstraShortestPath(g, "A", "E");

        string[] path = s.GenerateShortestPath("A", "E");
    }
}

public class Solution
{
    private List<int> _visited = new List<int>();
    private Dictionary<string, int> _weightTracker = new Dictionary<string, int>();
    private Dictionary<string, string> _parentTracker = new Dictionary<string, string>();
    PriorityQueue<string, int> _queue = new PriorityQueue<string, int>();

    public int DijkstraShortestPath(Dictionary<string, List<Node>> graph, string startNode, string endNode)
    {
        //init weight tracker
        InitWeightTracker(graph, startNode);

        //init parent tracker
        InitParentTracker(graph);

        //queue start node
        _queue.Enqueue(startNode, 0);

        while(_queue.Count > 0)
        {
            //dequeue node

            string currentNode = _queue.Dequeue();

            //get node weight
            int currentNodeWeight = _weightTracker[currentNode];

            //loop through neighbour
            foreach(var neighbour in graph[currentNode])
            {

                //for each neighbour,

                    //relaxation

                    //get d[u] + w(u + v). node weight + edge weight
                    int wuv = currentNodeWeight + neighbour.Weight;

                    //get neighbour weight
                    int neighbourWeight = _weightTracker[neighbour.Label];

                    if(wuv < neighbourWeight)
                    {
                        //update neighbour weight
                        _weightTracker[neighbour.Label] = wuv;

                        //update parent of neighbour
                        _parentTracker[neighbour.Label] = currentNode;

                        //queue neighbour
                        _queue.Enqueue(neighbour.Label, wuv);
                    }
                        
            }

            // add to visited
        }


        return _weightTracker[endNode];
    }

    public string[] GenerateShortestPath(string start, string end)
    {
        var path = new List<string>();

        path.Add(end);

        string parent = _parentTracker[end];

        if(string.IsNullOrEmpty(parent))
            return path.ToArray();

        while(parent != "")
        {
            path.Add(parent);

            if(_parentTracker.ContainsKey(parent))
                parent = _parentTracker[parent];
            else
                parent = "";
        }

        path.Reverse();

        return path.ToArray(); 
    }

    private void InitWeightTracker(Dictionary<string, List<Node>> graph, string startNode)
    {
        _weightTracker[startNode] = 0;

        foreach(var key in graph.Keys)
        {
            if(key != startNode)
                _weightTracker[key] = int.MaxValue;
        }
    }

    private void InitParentTracker(Dictionary<string, List<Node>> graph)
    {
        foreach(var key in graph.Keys)
        {
            _parentTracker[key] = "";
        }
    }
}

public class Node
{
    public Node(string label, int weight)
    {
        Label = label;
        Weight = weight;
    }
    public string Label { get; set; }
    public int Weight { get; set; }
}