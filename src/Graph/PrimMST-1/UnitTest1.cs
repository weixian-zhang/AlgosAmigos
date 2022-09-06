namespace PrimMST_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new Dictionary<Node, List<Node>>();
        g[new Node(0,0)] = new List<Node>() { new Node(1, 10), new Node(2, 1), new Node(3, 4) };
        g[new Node(1,0)] = new List<Node>() { new Node(0, 10), new Node(2, 3), new Node(4, 0) };
        g[new Node(2,0)] = new List<Node>() { new Node(2, 0), new Node(1, 3), new Node(3, 2), new Node(5, 8) };
        g[new Node(3,0)] = new List<Node>() { new Node(0, 4), new Node(2, 2), new Node(5, 2), new Node(6, 7) };
        g[new Node(4,0)] = new List<Node>() { new Node(1, 0), new Node(5, 1), new Node(7, 8) };
        g[new Node(5,0)] = new List<Node>() { new Node(2, 8), new Node(4, 1), new Node(3, 2), new Node(6, 6), new Node(7, 9) };
        g[new Node(6,0)] = new List<Node>() { new Node(3, 7), new Node(5, 6), new Node(7, 12) };
        g[new Node(7,0)] = new List<Node>() { new Node(4, 8), new Node(5, 9), new Node(6, 12) };


        var s = new Solution();

        var mstPath = s.PrimMST(g, 0, 8);

        string path = "";
        int cost = 0;
        foreach(var n in mstPath)
        {
            path += $"parent: {n.ParentLabel} -> node: {n.Label} | ";
            cost += n.Weight;
        }
        Console.WriteLine(path);
        Console.WriteLine($"Cost = {cost}");
    }
}

public class Solution
{
    
    

    //returns minimim psanning tree adjacency List and cost
    public List<Node> PrimMST(Dictionary<Node, List<Node>> graph, int startNode, int totalNodes)
    {
        int edgeCount = 0;
        
        var mst = new List<Node>();

        int totalCost = 0;
        var _visited = new List<int>();
        var minPQ = new PriorityQueue<Node, int>();
        int treeEdges = totalNodes - 1;

        _visited.Add(startNode);
        foreach(var n in graph[new Node(startNode, 0)])
        {
            minPQ.Enqueue(n, n.Weight);
        }

        var currentParent = new Node();
        var _parent = new Dictionary<int,int>();

        currentParent = new Node(startNode, 0);

        while(minPQ.Count > 0 && edgeCount <= treeEdges)
        {
            Node currentNode = minPQ.Dequeue();

            //ignore if visited
            if(_visited.Contains(currentNode.Label))
                continue;

            //add node to mstSet to build up spanning tree from scratch
            mst.Add(currentNode);

            totalCost += currentNode.Weight;  //for convenience total weight

            edgeCount++;                   //increment edge, if edge reaches (total nodes - 1), a tree is form
        
            //greedily add other neighbours to visit next in priority
            foreach(var neighbour in graph[currentNode])
            {
                if(!_visited.Contains(currentNode.Label))
                {
                    neighbour.ParentLabel = currentNode.Label; //track parent

                    minPQ.Enqueue(neighbour, neighbour.Weight);
                }
            }

            _visited.Add(currentNode.Label);
        }

        return mst;

    }
}

public class Node
{
    public Node() {}

    public Node(int label, int weight)
    {
        Label = label;
        Weight = weight;
    }
    public int Label { get; set; }
    public int Weight { get; set; }
    public int ParentLabel { get; set; }

    public override bool Equals(object? obj)
    {
        var n = obj as Node;
        if(n == null)
            return false;
        return n.Label == this.Label;
    }

    public override int GetHashCode()
    {
        return this.Label.GetHashCode();
    }
}