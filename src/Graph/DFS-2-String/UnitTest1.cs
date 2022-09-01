namespace DFS_2_String;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var graph = new Dictionary<string, List<TreeNode<string>>>();

        graph["Alice"] = new List<TreeNode<string>>() { new TreeNode<string>("Bob"), 
            new TreeNode<string>("Candy"), new TreeNode<string>("Derek"), new TreeNode<string>("Elain") };

        graph["Bob"] = new List<TreeNode<string>>() { new TreeNode<string>("Fred"), new TreeNode<string>("Helen")};

        graph["Fred"] = new List<TreeNode<string>>() { new TreeNode<string>("Helen")};

        graph["Helen"] = new List<TreeNode<string>>() { };

        graph["Candy"] = new List<TreeNode<string>>() { new TreeNode<string>("Helen")};

        graph["Derek"] = new List<TreeNode<string>>() { new TreeNode<string>("Elain"), new TreeNode<string>("Gina") };

        graph["Elain"] = new List<TreeNode<string>>() { };

        graph["Gina"] = new List<TreeNode<string>>() { new TreeNode<string>("Irena")};

        graph["Irena"] = new List<TreeNode<string>>() { };

        var s  = new Solution();
        //string[] path1 = s.DFSRecurseString(graph, new TreeNode<string>("Alice"));

        string[] path2 = s.DFSStack(graph, new TreeNode<string>("Alice"));
    }

    public class Solution
    {
        private List<string> visited = new List<string>();

        public string[] DFSRecurseString(Dictionary<string, List<TreeNode<string>>> graph, TreeNode<string> node)
        {
            visited.Add(node.Label);

            foreach(var neighbour in graph[node.Label])
            {
                if(!visited.Contains(neighbour.Label))
                {
                    DFSRecurseString(graph, neighbour);
                }
            }


            return visited.ToArray();
        }

        Stack<string> stack = new Stack<string>();
        public string[] DFSStack(Dictionary<string, List<TreeNode<string>>> graph, TreeNode<string> node)
        {
            stack.Push(node.Label);

            while(stack.Count > 0)
            {
                string nextNeighbour = stack.Pop();
                visited.Add(nextNeighbour);

                if(graph[nextNeighbour] != null)
                {
                    foreach(var neighbour in graph[nextNeighbour])
                    {
                        if(!visited.Contains(neighbour.Label))
                            stack.Push(neighbour.Label);
                    }
                    
                }
            }

            return visited.ToArray();
        }
    }


    public class TreeNode<T>
    {
        public TreeNode(T label)
        {
            Label = label;
        }
        public T Label { get; set; }
        public int Cost { get; set; }
    }
}