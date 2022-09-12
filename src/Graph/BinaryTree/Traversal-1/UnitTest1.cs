namespace Traversal_1;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        // var root = new Node<int>(1);
        // var node2 = new Node<int>(2);
        // var node3 = new Node<int>(3);
        // var node4 = new Node<int>(4);
        // var node5 = new Node<int>(5);
        
        // root.Left = node2;
        // root.Right = node3;
        // node2.Left = node4;
        // node2.Right = node5;

        var s1 = new InPrePostTraversal();
        //int[] r = s1.InOrder(root);
        //int[] r = s1.PreOrder(root);
        //int[] r = s1.PostOrder(root);

        var a = new Node<string>("a");
        var b = new Node<string>("b");
        var c = new Node<string>("c");
        var d = new Node<string>("d");
        var e = new Node<string>("e");
        var f = new Node<string>("f");
        var h = new Node<string>("h");
        var i = new Node<string>("i");
        var j = new Node<string>("j");
        var k = new Node<string>("k");
        var l = new Node<string>("l");
        var m = new Node<string>("m");
        var n = new Node<string>("n");
        var o = new Node<string>("o");
        var u = new Node<string>("u");
        
        a.Left = b;
        a.Right = c;
        b.Left = d;
        b.Right = e;
        c.Left = u;
        c.Right = f;
        d.Left = h;
        d.Right = i;
        e.Left = j;
        e.Right = k;
        u.Left = l;
        u.Right = m;
        f.Left = n;
        f.Right = o;


    //     a
    //     /\
    //    b   c
    //    /\    \
    //  d   e    f

        // var s3 = new DFSTraversal();
        // var r = new List<string>();
        // s3.DFS(a, r);


        // var s2 = new BinaryTreeSerializer();
        // var r = s2.Serialize(a);
        // Node<String> root = s2.Deserialize(r, 0);
    }

   
}

public class DFSTraversal
{
    List<string> result = new List<string>();

    public string[] DFS(Node<string> node, List<string> result)
    {
        if(node == null)
        {
            return result.ToArray();
        }

        

        if(node.Left != null)
            DFS(node.Left , result);
        //to serialize to array, tree has to be a full tree. check if right has node then Left must be null
        else if(node.Left == null && node.Right != null)
            result.Add(null);
     
        
        
        if(node.Right != null)
            DFS(node.Right , result);
        //to serialize to array, tree has to be a full tree. check if Left has node then Right must be null
        else if(node.Right == null && node.Left != null)
            result.Add(null);

        if(node != null)
            result.Add(node.Value);

        return result.ToArray();

    }
}

public class BinaryTreeSerializer
{
    Queue<Node<string>> _queue = new Queue<Node<string>>();

    public string[] Serialize(Node<string> node)
    {
        _queue.Enqueue(node);

        var r = new List<string>();

        while(_queue.Count > 0)
        {
            var n = _queue.Dequeue();

            r.Add(n.Value);

            if(n.Left != null)
                _queue.Enqueue(n.Left);

            if(n.Right != null)
                _queue.Enqueue(n.Right);

        }

        return r.ToArray();
    }

    public Node<String> Deserialize(string[] arr, int i)
    {
        Node<String> root = null;

        // Base case for recursion
        if (i < arr.Length) 
        {
            var temp = new Node<String>(arr[i]);
            root = temp;
  
            // insert left child
            root.Left = Deserialize(arr, 2 * i + 1);
  
            // insert right child
            root.Right = Deserialize(arr, 2 * i + 2);
        }
        return root;
    }
}

public class InPrePostTraversal
{
    public int[] InOrder(Node<int> node)
    {
        var result = new List<int>();
        return InOrderInternal(node, result);
    }

    // left, root right
    private int[] InOrderInternal(Node<int> node, List<int> result)
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

    public int[] PreOrder(Node<int> node)
    {
        var r = new List<int>();
        return PreOrderInternal(node, r);
    }

    //root left right
    private int[] PreOrderInternal(Node<int> node, List<int> result)
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

    public int[] PostOrder(Node<int> node)
    {
        var r = new List<int>();
        return PostOrderInternal(node, r);
    }

    //left right root
    private int[] PostOrderInternal(Node<int> node,  List<int> result)
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

public class Node<T>
{
    public Node(T value)
    {
        Value = value;
    }
    public T Value { get; set; }
    public Node<T> Left { get; set; }
    public Node<T> Right { get; set; }
}