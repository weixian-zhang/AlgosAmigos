namespace Graph;
public class Graph
{
    Dictionary<int, List<TreeNode>> graph;

    public Graph()
    {
        graph = new Dictionary<int, List<TreeNode>>();
    }

    public List<TreeNode> this[int index]
    {
        get
        {
            return graph[index];
        }

        set
        {
            graph[index] = value;
        }
    }
}


