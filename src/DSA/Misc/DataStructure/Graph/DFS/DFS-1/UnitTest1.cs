namespace DFS_1;

public class UnitTest1
{
    //practice 1
    // https://practice.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

    [Fact]
    public void Test1()
    {
        // graph dict
        // var g = new Dictionary<int, List<TreeNode>>();
        // g[0] = new List<TreeNode>() {new TreeNode(1), new TreeNode(2), new TreeNode(3)};
        // g[1] = new List<TreeNode>() {}; 
        // g[2] = new List<TreeNode>() {new TreeNode(4)}; 
        // g[3] = new List<TreeNode>() {};
        // g[4] = new List<TreeNode>() {new TreeNode(2)};

        var g = new Dictionary<int, List<TreeNode>>();
        g[1] = new List<TreeNode>() {new TreeNode(4), new TreeNode(2)};
        g[2] = new List<TreeNode>() {new TreeNode(3), new TreeNode(5),new TreeNode(7), new TreeNode(8)}; 
        g[3] = new List<TreeNode>() {new TreeNode(4),new TreeNode(9), new TreeNode(10)}; 
        g[4] = new List<TreeNode>() {new TreeNode(1), new TreeNode(3)};
        g[5] = new List<TreeNode>() {new TreeNode(6),new TreeNode(7), new TreeNode(8)}; 
        g[6] = new List<TreeNode>() {}; 
        g[7] = new List<TreeNode>() {new TreeNode(5),new TreeNode(8)}; 
        g[8] = new List<TreeNode>() {new TreeNode(2), new TreeNode(5),new TreeNode(7)}; 
        g[9] = new List<TreeNode>() {new TreeNode(3)}; 
        g[10] = new List<TreeNode>() {new TreeNode(3)}; 

        var s = new Solution();

        int[] path = s.DFSRecurse(g, new TreeNode(1));

        int[] path2 = s.DFSStack(g, new TreeNode(1));
    }

    public class Solution
    {
        private List<int> visited = new List<int>();

        public int[] DFSRecurse(Dictionary<int, List<TreeNode>> graph, TreeNode node)
        {
            visited.Add(node.Label);

            if(graph[node.Label] != null)
            {
                foreach(var neighbour in graph[node.Label])
                {
                    if(!visited.Contains(neighbour.Label))
                    {
                        //result.Add(neighbour.Label);

                        DFSRecurse(graph, neighbour);
                    }
                
                }
            }
            

            return visited.ToArray();
        }

        private Stack<TreeNode> stack = new Stack<TreeNode>();

        public int[] DFSStack(Dictionary<int, List<TreeNode>> graph, TreeNode nextNodeToTraverse)
        {
            
            stack.Push(nextNodeToTraverse);

            while(stack.Count() > 0)
            {

                var nextItemCouldBeVisitedBefore = stack.Peek();
                if(visited.Contains(nextItemCouldBeVisitedBefore.Label))
                {
                    stack.Pop();
                    continue;
                }
                    

                var node = stack.Pop();
                visited.Add(node.Label);

                if(graph[node.Label] != null) {
                    foreach(var n in graph[node.Label])
                    {
                        stack.Push(n);
                    }
                }
            }

            return visited.ToArray();
            
        }
    }

    



    public class TreeNode
    {
        public TreeNode(int label)
        {
            Label = label;
        }

        public int Label { get; set; }
        public int Weight { get; set; }
    }

    // public class GraphEdgeList
    // {
    //     LinkedList<int>[] adjList = new LinkedList<int>[]{};
    //     public void AddEdge(int nodeLabel, int edgeLabel)
    //     {
    //         var nodeExist = adjList[nodeLabel];

    //         if(nodeExist == null)
    //         {
    //             adjList[nodeLabel] = new LinkedList<int>();
    //             adjList[nodeLabel].AddFirst(nodeLabel);
    //         }
    //         else
    //         {
    //             var last = adjList[edgeLabel].Last;

    //             if(last != null)
    //                 adjList[nodeLabel].AddAfter(last, edgeLabel);
    //         }
                
    //     }
    // }
}