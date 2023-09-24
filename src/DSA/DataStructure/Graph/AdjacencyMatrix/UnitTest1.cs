using System.Text;

namespace AdjacencyMatrix;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var g = new AdjacencyMatrixGraph();

        g.AddNode("0");
        g.AddNode("1");
        g.AddNode("2");
        g.AddNode("3");
        g.AddNode("4");
        g.AddNode("5");
        g.AddNode("6");
        g.AddNode("7");

        g.AddEdge("0", "1", 10);
        g.AddEdge("0", "2", 1);
        g.AddEdge("0", "3", 4);

        g.AddEdge("1", "0", 10);
        g.AddEdge("1", "2", 3);
        g.AddEdge("1", "4", 0);

        g.AddEdge("2", "0", 1);
        g.AddEdge("2", "1", 3);
        g.AddEdge("2", "3", 2);
        g.AddEdge("2", "5", 8);

        g.AddEdge("3", "0", 4);
        g.AddEdge("3", "2", 2);
        g.AddEdge("3", "5", 2);
        g.AddEdge("3", "6", 7);

        g.AddEdge("4", "1", 0);
        g.AddEdge("4", "5", 1);
        g.AddEdge("4", "7", 8);

        g.AddEdge("5", "2", 8);
        g.AddEdge("5", "3", 2);
        g.AddEdge("5", "4", 1);
        g.AddEdge("5", "6", 6);
        g.AddEdge("5", "7", 9);

        g.AddEdge("6", "3", 7);
        g.AddEdge("6", "5", 6);
        g.AddEdge("6", "7", 12); 

        g.AddEdge("7", "4", 8);
        g.AddEdge("7", "5", 9);
        g.AddEdge("7", "6", 12); 

        var pmst = new PrimMST();
        int cost = pmst.FindMST(g);


        g.PrintMatrix();
    }
}

public class PrimMST
{
    private PriorityQueue<Node, int> _minPQ = new  PriorityQueue<Node, int>();
    private List<string> _visited = new List<string>();
    private List<Node> _mst = new List<Node>();

    public int FindMST(AdjacencyMatrixGraph g)
    {
        var startNode = new Node("0");

        _minPQ.Enqueue(startNode, 0);

        int cost = 0;

        while(_minPQ.Count > 0)
        {
            var currentNode = _minPQ.Dequeue();

            if(_visited.Contains(currentNode.Label))
                continue;

            
            _mst.Add(currentNode);
            cost += currentNode.Weight;

            var neighbours = g.GetNeighbours(currentNode.Label);
            foreach(var n in neighbours)
            {
                if(_visited.Contains(n.Label))
                    continue;

                _minPQ.Enqueue(n, n.Weight);
            }

             _visited.Add(currentNode.Label);
        }

        return cost;
    }
}


public class AdjacencyMatrixGraph
{
    private List<Node> _nodes = new List<Node>();
    int[,] _adjMatrix = null;

    public List<Node> GetNeighbours(string label)
    {
        int index = GetNodeIndex(label);
        var result=  new List<Node>();

        for(int col = 0; col <= _nodes.Count - 1; col++)
        {
            int weight = _adjMatrix[index, col];

            if(weight != int.MinValue)
            {
                var neighbourNode = GetNodeByIndex(col);
                neighbourNode.Weight = weight;
                result.Add(neighbourNode);
            }
        }

        return result;
    }

    public Node GetNodeByIndex(int index)
    {
        var node = _nodes.ToArray()[index];
        return new Node(node.Label, node.Weight);
    }

    public void AddNode(string label)
    {
        _nodes.Add(new Node(label));
    }

    public void AddEdge(string xNodeLabel, string yNodeLabel, int weight)
    {
        InitAdjMatrix();

        int x = GetNodeIndex(xNodeLabel);
        int y = GetNodeIndex(yNodeLabel);

        if(x != -1 && y != -1)
        {
            _adjMatrix[x,y] = weight;
        }
    }

    public void PrintMatrix()
    {
        var sb = new StringBuilder();
        for(int x = 0; x <= _nodes.Count - 1; x++)
        {
            for(int y = 0; y <= _nodes.Count - 1; y++)
            {
                sb.Append($"{_adjMatrix[x,y].ToString()}, ");

                if(y == _nodes.Count - 1)
                    sb.Append(Environment.NewLine);
            }
        }

        Console.WriteLine(sb.ToString());
    }

    private void InitAdjMatrix()
    {
        int count = _nodes.Count;
        if(_adjMatrix == null)
        {
            _adjMatrix = new int[count, count];

            for(int row = 0; row < _nodes.Count; row++)
            {
                for (int col = 0; col < _nodes.Count; col++)
                {
                    _adjMatrix[row, col] = int.MinValue;
                }
            }
        }
    }

    private int GetNodeIndex(string nodeLabel)
    {
        if(_nodes.FirstOrDefault(x => x.Label == nodeLabel) == null)
            return -1;

        int index = _nodes.FindIndex(x => x.Label == nodeLabel);

        return index;
    }

    private bool TryGetNode(string nodeLabel, out Node node)
    {
        var n = _nodes.FirstOrDefault(x => x.Label == nodeLabel);
        if(n == null)
        {
            node = null;
            return false;
        }

        node = n;

        return true;

    }
}

public class Node
{
    public Node(string label)
    {
        Label = label;
    }

    public Node(string label, int weight)
    {
        Label = label;
        Weight = weight;
    }

    public string Label { get; set; }
    public int Weight { get; set; }
}