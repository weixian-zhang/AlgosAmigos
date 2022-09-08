namespace KruskalMST_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new Dictionary<Node, List<Node>>();
        g[new Node(0,0)] = new List<Node>() { new Node(1, 10), new Node(2, 1), new Node(3, 4) };
        g[new Node(1,0)] = new List<Node>() { new Node(0, 10), new Node(2, 3), new Node(4, 0) };
        g[new Node(2,0)] = new List<Node>() { new Node(0, 1), new Node(1, 3), new Node(3, 2), new Node(5, 8) };
        g[new Node(3,0)] = new List<Node>() { new Node(0, 4), new Node(2, 2), new Node(5, 2), new Node(6, 7) };
        g[new Node(4,0)] = new List<Node>() { new Node(1, 0), new Node(5, 1), new Node(7, 8) };
        g[new Node(5,0)] = new List<Node>() { new Node(2, 8), new Node(4, 1), new Node(3, 2), new Node(6, 6), new Node(7, 9) };
        g[new Node(6,0)] = new List<Node>() { new Node(3, 7), new Node(5, 6), new Node(7, 12) };
        g[new Node(7,0)] = new List<Node>() { new Node(4, 8), new Node(5, 9), new Node(6, 12) };

        var s = new Solution();

        s.KruskalMST(g);

        //init DisjointSet

        // g.Add(new Tuple<Node, Node, int>(new Node(0), new Node(1), 10));
        // g.Add(new Tuple<Node, Node, int>(new Node(0), new Node(2), 1));
        // g.Add(new Tuple<Node, Node, int>(new Node(0), new Node(3), 4));

        // g.Add(new Tuple<Node, Node, int>(new Node(1), new Node(0), 10));
        // g.Add(new Tuple<Node, Node, int>(new Node(1), new Node(2), 3));
        // g.Add(new Tuple<Node, Node, int>(new Node(1), new Node(4), 0));

        // g.Add(new Tuple<Node, Node, int>(new Node(2), new Node(2), 0));
        // g.Add(new Tuple<Node, Node, int>(new Node(2), new Node(1), 3));
        // g.Add(new Tuple<Node, Node, int>(new Node(2), new Node(3), 2));
        // g.Add(new Tuple<Node, Node, int>(new Node(2), new Node(5), 8));

        // g.Add(new Tuple<Node, Node, int>(new Node(3), new Node(0), 4));
        // g.Add(new Tuple<Node, Node, int>(new Node(3), new Node(2), 2));
        // g.Add(new Tuple<Node, Node, int>(new Node(3), new Node(5), 2));
        // g.Add(new Tuple<Node, Node, int>(new Node(3), new Node(6), 7));

        // g.Add(new Tuple<Node, Node, int>(new Node(4), new Node(1), 0));
        // g.Add(new Tuple<Node, Node, int>(new Node(4), new Node(5), 1));
        // g.Add(new Tuple<Node, Node, int>(new Node(4), new Node(7), 8));

        // g.Add(new Tuple<Node, Node, int>(new Node(5), new Node(2), 8));
        // g.Add(new Tuple<Node, Node, int>(new Node(5), new Node(4), 1));
        // g.Add(new Tuple<Node, Node, int>(new Node(5), new Node(3), 2));
        // g.Add(new Tuple<Node, Node, int>(new Node(5), new Node(6), 6));
        // g.Add(new Tuple<Node, Node, int>(new Node(5), new Node(7), 9));

        // g.Add(new Tuple<Node, Node, int>(new Node(6), new Node(3), 7));
        // g.Add(new Tuple<Node, Node, int>(new Node(6), new Node(5), 6));
        // g.Add(new Tuple<Node, Node, int>(new Node(6), new Node(7), 12));

        // g.Add(new Tuple<Node, Node, int>(new Node(7), new Node(4), 8));
        // g.Add(new Tuple<Node, Node, int>(new Node(7), new Node(5), 96));
        // g.Add(new Tuple<Node, Node, int>(new Node(7), new Node(6), 12));

        // g = g.OrderBy(x => x.Item3).ToList();
        
    }
}

public class Solution
{
    private List<Tuple<Node, Node, int>> _nodePairs = new List<Tuple<Node, Node, int>>();
    private DisjointSet _disjointSet = new DisjointSet();

    private List<Tuple<Node, Node, int>> _result = new List<Tuple<Node, Node, int>>();

    public List<Tuple<Node, Node, int>> KruskalMST(Dictionary<Node, List<Node>> graph)
    {
        int cost = 0;

        Init(graph);

        foreach(var nodes in _nodePairs)
        {
            var nodeX = nodes.Item1;
            var nodeY = nodes.Item2;

            //union sets, nodes that are ignored will
            if(_disjointSet.Union(nodeX.ID, nodeY.ID))
            {
                cost += nodeY.Weight;
                _result.Add(new Tuple<Node, Node, int>(nodeX, nodeY, nodeY.Weight));
            }
            else
                Console.WriteLine($"not in set {nodeX.ID},{nodeY.ID}");
        }

        return _result;
    }

    private void Init(Dictionary<Node, List<Node>> g)
    {
        foreach(var u in g)
        {
            var node = u.Key;

            foreach(var e in u.Value )
            {
                var edge = e;

                var pair = new Tuple<Node, Node, int>(node, edge, edge.Weight);
                _nodePairs.Add(pair);
            }
        }
        _nodePairs = _nodePairs.OrderBy(x => x.Item3).ToList();

        var disjoinSet = new DisjointSet();
        
        foreach(var kv in g)
        {
            var node = kv.Key;
            _disjointSet.MakeSet(node.ID);
        }
    }
}

public class DisjointSet
{
    
    private Dictionary<int, Node> map = new Dictionary<int, Node>();

    public void MakeSet(int nodeId)
    {
        var node = new Node(nodeId);
        node.Parent = node;
        map.Add(nodeId, node);
    }

    public bool Union(int xNodeId, int yNodeId)
    {
        var nodeX = map[xNodeId];
        var nodeY = map[yNodeId];

        var rootParentX = FindSet(nodeX.ID);
        var rootParentY = FindSet(nodeY.ID);

        if(rootParentX.ID == rootParentY.ID) //check if both node already in same set, return false as both nodes cannot be union
            return false;

        if(rootParentX.Rank > rootParentY.Rank)
        {
            rootParentY.Parent = rootParentX;
        }
        else if(rootParentX.Rank < rootParentY.Rank)
        {
            rootParentX.Parent = rootParentY;
        }
        else
        {
            rootParentY.Parent = rootParentX;
            rootParentX.Rank += 1;
        }

        return true;
    }

    //always returns root parent node
    public Node FindSet(int nodeId)
    {
        var node = map[nodeId];

        //base case = if parent equals to node itself
        if(node.Parent == node)
            return node;

        var parent = FindSet(node.Parent.ID); //recursive;y find parent

        node.Parent = parent; //path compression, point node to root for faster Find in future

        return node.Parent;
    }
}

public class Node
{
    public Node(int id, int weight = 0, Node parent = null) 
    {
        ID = id;
        Weight = weight;
        Parent = parent ?? this;
    }
    public int ID { get; set; }
    public int Weight { get; set; }
    public Node Parent { get; set; }
    public int Rank { get; set; } = 0;
}