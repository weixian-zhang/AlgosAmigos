using System.Collections;

namespace Dijkstra;

public class UnitTest1
{
    [Fact]
    public void Run()
    {
        var dj = new Dijkstra();

        string path = dj.FindShortestPath("start", "finish");

        Console.WriteLine(path);
    }
}

public class Node
{
    public Node(string name)
    {
        Name = name;
    }

    public Node(string name, int cost)
    {
        Name = name;
        Cost = cost;
    }

    public string Name { get; set; } = "";
    public int Cost { get; set; } = -1;
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
    private Dictionary<string,int> _costTracker = new Dictionary<string,int>();
    private Hashtable _parentTracker = new Hashtable();
    private PriorityQueue<string, int> _pqueue = new PriorityQueue<string, int>();

    public string FindShortestPath(string startNode, string endNode)
    {
        var graph = new Dictionary<string, List<Node>>();

        graph["start"] = new List<Node>() { new Node("a", 6), new Node("b", 2) };

        graph["a"] = new List<Node>() { new Node("b", 3), new Node("finish", 1) };

        graph["b"] = new List<Node>() { new Node("a", 3), new Node("finish", 5) };

        InitNodeWeightParentTrackerPriorityQueue(graph, startNode, endNode);

        while(_pqueue.Count != 0) {

            string currentNode= _pqueue.Dequeue();

            if(!graph.ContainsKey(currentNode)) // node has no neighbours
                continue;

            foreach(var neighbour in graph[currentNode])
            {
                int currentNodeWeight =  GetNodeCost(currentNode);

                EnqueueNodeIfNotVisited(neighbour.Name, neighbour.Cost);

                if(neighbour.Name != endNode && !IsNodeCostSet(neighbour.Name)) {   // cost was not initialize
                     UpdateNodeWeight(neighbour.Name, neighbour.Cost);
                     continue;
                }

                //cost was initialize for neighbour, continue

                int neighbourCost = GetNodeCost(neighbour.Name);

                int alternatePathCost = neighbour.Cost + currentNodeWeight;
                
                if (alternatePathCost < neighbourCost) { //found shorter route

                    UpdateNodeWeight(neighbour.Name, alternatePathCost); //update weight tracker with shorter weight

                    updateParent(neighbour.Name, currentNode);
                }
            }

            MarkNodeVisited(currentNode);
        }

        string path = GenerateResult(endNode);

        return path;
        
    }

    private void EnqueueNodeIfNotVisited(string node, int cost)
    {
        if(!IsVisited(node))
            _pqueue.Enqueue(node, cost);
    }

    private bool IsNodeCostSet(string node)
    {
        if(_costTracker[node] == int.MaxValue)
            return false;
        
        return true;
    }

    private string GenerateResult(string endNode)
    {
        var path = new List<string>();

        string parent = _parentTracker[endNode].ToString();

        path.Add($"{endNode}:{GetNodeCost(endNode)}");
        path.Add($"{parent}:{GetNodeCost(parent)}");

        while(parent != "")
        {
            if(_parentTracker.ContainsKey(parent)) {
                parent = _parentTracker[parent].ToString();

                if(parent != "")
                    path.Add($"{parent}:{GetNodeCost(parent)}");
            }
        }

        path.Reverse();

        return string.Join(",", path);
    }

    private void InitNodeWeightParentTrackerPriorityQueue(Dictionary<string, List<Node>> graph, string startNode, string endNode)
    {
        _costTracker[startNode] = 0;
        _costTracker[endNode] = int.MaxValue;

        _pqueue.Enqueue(startNode, 0);

        foreach(var nodeName in graph.Keys)
        {
            _parentTracker[nodeName] = "";

            if(nodeName != startNode && nodeName != endNode) { //ignore start and finish nodes

                _costTracker[nodeName] = int.MaxValue;

            }
        }
    }

    private int GetNodeCost(string nodeName)
    {
        int weight = (int) _costTracker[nodeName];
        
        return weight;
    }

    private void UpdateNodeWeight(string node, int newWeight)
    {
        _costTracker[node] = newWeight;
    }

    private void updateParent(string node, string parent)
    {
        _parentTracker[node] = parent;
    }

    private void MarkNodeVisited(string nodeName)
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