namespace Traversal_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var root = new Node(1);
        var node2 = new Node(2);
        var node3 = new Node(3);
        var node4 = new Node(4);
        var node5 = new Node(5);

        root.Left = node2;
        root.Right = node3;

        node2.Left = node4;
        node2.Right = node5;


        var s = new Solution();

        //int[] r = s.InOrder(root);

        //int[] r = s.PreOrder(root);

        int[] r = s.PostOrder(root);
    }
}

public class Solution
{
    public int[] InOrder(Node node)
    {
        var result = new List<int>();
        return InOrderInternal(node, result);
    }

    // left, root right
    private int[] InOrderInternal(Node node, List<int> result)
    {   
        if(node == null)
            return result.ToArray();

        if(node.Left != null)
            InOrderInternal(node.Left, result);

        result.Add(node.Value);

        if(node.Right != null) 
            InOrderInternal(node.Right, result);

        return result.ToArray();
    }

    public int[] PreOrder(Node node)
    {
        var r = new List<int>();
        return PreOrderInternal(node, r);
    }

    //root left right
    private int[] PreOrderInternal(Node node, List<int> result)
    {
        if(node == null)
            return result.ToArray();

        result.Add(node.Value);

        if(node.Left != null)
            PreOrderInternal(node.Left, result);

        if(node.Right != null)
            PreOrderInternal(node.Right, result);

        return result.ToArray();
    }

    public int[] PostOrder(Node node)
    {
        var r = new List<int>();
        return PostOrderInternal(node, r);
    }

    //left right root
    private int[] PostOrderInternal(Node node,  List<int> result)
    {
        if(node == null)
            return result.ToArray();

        if(node.Left != null)
            PostOrderInternal(node.Left, result);

        if(node.Right != null)
            PostOrderInternal(node.Right, result);

        result.Add(node.Value);
        
        return result.ToArray();
    }
}

public class Node
{
    public Node(int value)
    {
        Value =value;
    }
    public int Value { get; set; }
    public Node Left { get; set; }
    public Node Right { get; set; }
}