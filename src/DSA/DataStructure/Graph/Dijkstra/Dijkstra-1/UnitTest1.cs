using System.Collections;

namespace Dijkstra;

public class UnitTest1
{

    [Fact]
    public void Dijkstra_Test_1()
    {
        var graph = new Dictionary<string, List<Node>>();

        graph["start"] = new List<Node>() { new Node("a", 5), new Node("b", 2) };

        graph["a"] = new List<Node>() { new Node("b", 8), new Node("z", 4), new Node("x", 2) };

        graph["b"] = new List<Node>() { new Node("a", 8), new Node("x", 7) };

        graph["z"] = new List<Node>() { new Node("a", 4), new Node("x", 6), new Node("finish", 3)  };

        graph["x"] = new List<Node>() { new Node("b", 7), new Node("a", 2), new Node("z", 6), new Node("finish", 1) };

        var dj = new Dijkstra();

        DijkstraResult result = dj.FindShortestPath(graph, "start", "finish");

        Assert.True(result.Cost == 8);

        Console.WriteLine(result.Path);
    }

    [Fact]
    public void Dijkstra_Test_2()
    {
        var graph = new Dictionary<string, List<Node>>();

        graph["z"] = new List<Node>() { new Node("b", 1) };

        graph["b"] = new List<Node>() { new Node("d", 2), new Node("x", 1) };

        graph["x"] = new List<Node>() { new Node("b", 1), new Node("d", 1) };

        graph["d"] = new List<Node>() { new Node("b", 2), new Node("x", 1), new Node("finish", 3) };

        var dj = new Dijkstra();

        DijkstraResult result = dj.FindShortestPath(graph, "z", "finish");

        Assert.True(result.Cost == 6);

        Console.WriteLine(result.Path);
    }

    [Fact]
    public void Dijkstra_Test_3()
    {
        var graph = new Dictionary<string, List<Node>>();

        graph["start"] = new List<Node>() { new Node("y", 2), new Node("z", 2) };

        graph["z"] = new List<Node>() { new Node("y", 2), new Node("x", 2), new Node("finish", 2) };

        graph["y"] = new List<Node>() { new Node("z", 2), new Node("x", 1) };

        graph["x"] = new List<Node>() { new Node("y", 1), new Node("z", 2), new Node("finish", 2) };

        var dj = new Dijkstra();

        DijkstraResult result = dj.FindShortestPath(graph, "start", "finish");

        Assert.True(result.Cost == 4);

        Console.WriteLine(result.Path);
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

public class DijkstraResult
{
    public string Path { get; set; } = "";
    public int Cost { get; set; } = 0;
}



public class Dijkstra
{
    private Hashtable _visitedNodes = new Hashtable();
    private Dictionary<string,int> _costTracker = new Dictionary<string,int>();
    private Hashtable _parentTracker = new Hashtable();
    private PriorityQueue<string, int> _pqueue = new PriorityQueue<string, int>();

    public DijkstraResult FindShortestPath(Dictionary<string, List<Node>> graph, string startNode, string endNode)
    {
        InitNodeWeightParentTrackerPriorityQueue(graph, startNode, endNode);

        while(_pqueue.Count != 0) {

            string currentNode= _pqueue.Dequeue();

            if(!graph.ContainsKey(currentNode))
                continue;

            foreach(var neighbour in graph[currentNode])
            {
                int currentNodeCost=  GetNodeCost(currentNode);

                //cost was initialize for neighbour, continue

                int neighboutEdgeCost = neighbour.Cost; //edge cost

                int alternatePathCost = neighboutEdgeCost + currentNodeCost;

                //for first time cost initialization, cost is not init when its int.max
                if(neighbour.Name != endNode && !IsNodeCostSet(neighbour.Name)) {   
                     UpdateNodeWeight(neighbour.Name, alternatePathCost);

                     updateParent(neighbour.Name, currentNode);

                     EnqueueNodeIfNotVisited(neighbour.Name, alternatePathCost);
                }

                int neighbourCost = GetNodeCost(neighbour.Name);  //updated node cost and not infinity anymore

                //let priority queue have duplicate entry its OK, as this duplicate entries find out shorter alternate paths
                if (alternatePathCost < neighbourCost) { //found shorter route

                    UpdateNodeWeight(neighbour.Name, alternatePathCost); //update weight tracker with shorter weight

                    updateParent(neighbour.Name, currentNode);

                    EnqueueNodeIfNotVisited(neighbour.Name, alternatePathCost);
                }
            }

            MarkNodeVisited(currentNode);
        }

        var result = GenerateResult(endNode);

        return result;
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

    private DijkstraResult GenerateResult(string endNode)
    {
        var result = new DijkstraResult();

        var path = new List<string>();

        int endNodeCost = GetNodeCost(endNode);

        result.Cost = endNodeCost;

        string parent = _parentTracker[endNode].ToString();

        path.Add($"{endNode}:{endNodeCost}");
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

        result.Path = string.Join(",", path);

        return result;
    }

    private void InitNodeWeightParentTrackerPriorityQueue(Dictionary<string, List<Node>> graph, string startNode, string endNode)
    {
        _costTracker[startNode] = 0;
        _costTracker[endNode] = int.MaxValue;

        _pqueue.Enqueue(startNode, 0); //algorithm starts here, node with priority 0 will always be the first to dequeue 

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