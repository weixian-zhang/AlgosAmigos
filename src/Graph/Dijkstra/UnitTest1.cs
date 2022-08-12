using System.Collections;

namespace Dijkstra;

public class UnitTest1
{
    [Fact]
    public void Run()
    {
        var dj = new Dijkstra();

        dj.FindShortestPath();
    }
}

public class Node
{
    public Node(string name)
    {
        Name = name;
    }

    public Node(string name, int weight)
    {
        Name = name;
        Weight = weight;
    }

    public string Name { get; set; } = "";
    public int Weight { get; set; } = -1;
    public List<Node> Neighbours { get; set; } = new List<Node>();
}


public class Graph
{

    public List<Node> Nodes { get; set; } = new List<Node>();

    public void Add(Node node, params Node[] neighbours)
    {
        if (neighbours != null && neighbours.Count() > 0)
            node.Neighbours.AddRange(neighbours);

        Nodes.Add(node);
    }
}



public class Dijkstra
{
    private Hashtable _visitedNodes = new Hashtable();
    private Hashtable _nodeWeights = new Hashtable();
    private Hashtable _parentTracker = new Hashtable();
    private PriorityQueue<string, int> _pqueue = new PriorityQueue<string, int>();

    public void FindShortestPath()
    {
        var graph = new Dictionary<string, List<Node>>();

        graph["start"] = new List<Node>() { new Node("a", 6), new Node("b", 2) };

        graph["a"] = new List<Node>() { new Node("b", 3), new Node("finish", 1) };

        graph["b"] = new List<Node>() { new Node("a", 3), new Node("finish", 5) };

        InitNodeWeightAndParentTrackerAndPriorityQueue(graph);

        while(_pqueue.Count != 0) {

            string currentNode = _pqueue.Dequeue();

            MarkVisited(currentNode);

            foreach(var neighbour in graph[currentNode])
            {

            }

        }
        
    }

    private void InitNodeWeightAndParentTrackerAndPriorityQueue(Dictionary<string, List<Node>> graph)
    {
        foreach(var n in graph.Keys)
        {
            _nodeWeights[n] = int.MaxValue;

            foreach (var nn in graph[n])
            { 
                _pqueue.Enqueue(nn.Name, nn.Weight);
                _nodeWeights[nn.Name] = nn.Weight;
                _parentTracker[nn.Name] = n;
            }
        }
        _nodeWeights["finish"] = int.MaxValue;
    }

    private void MarkVisited(string nodeName)
    {
        if(!_visitedNodes.ContainsKey(nodeName))
            _visitedNodes[nodeName] = true;
    }

    private bool IsVisited(string nodeName)
    {
        if(_visitedNodes.ContainsKey(nodeName))
            return true;
        
        return false;
    }

    
}