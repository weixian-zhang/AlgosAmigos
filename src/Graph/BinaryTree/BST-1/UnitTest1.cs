namespace Traversal_1;

public class UnitTest1
{
    BinarySearchTree bt = new BinarySearchTree();
    TreeNode a50 = new TreeNode(50);
    TreeNode a35 = new TreeNode(35);
    TreeNode a67 = new TreeNode(67);
    TreeNode a20 = new TreeNode(20);
    TreeNode a40 = new TreeNode(40);
    TreeNode a11 = new TreeNode(11);
    TreeNode a28 = new TreeNode(28);
    
    public UnitTest1()
    {       
        a50.Left = a35;
        a50.Right = a67;
        a35.Left = a20;
        a35.Right = a40;
        a40.Left = a28;
        a28.Left = a11;
        
        bt.Root = a50;
    }


    [Fact]
    public void IsBST_True()
    {
        a50.Left = a35;
        a50.Right = a67;
        a35.Left = a20;
        a35.Right = a40;
        a40.Left = a28;
        
        bt.Root = a50;

        bool isItReallyBST = bt.IsBST();

        Assert.True(isItReallyBST);
    }

    [Fact]
    public void IsBST_False()
    {       
        a50.Left = a35;
        a50.Right = a35; //a67;
        a35.Left = a20;
        a35.Right = a40;
        a40.Left = a28;

        bt.Root = a50;

        bool isItReallyBST = bt.IsBST();

        Assert.False(isItReallyBST);
    }

   [Fact]
   public void MinValue()
   {
        var min = bt.MinValue();
   }

   [Fact]
   public void SearchNode_True()
   {
        var node = bt.Search(40);
   }
    
}

public class BinarySearchTree
{
    public TreeNode Root { get; set; }

    public TreeNode Add(int data)
    {
        if(Root == null)
        {
            Root = new TreeNode(data);
            return Root;
        }
        
        return AddInternal(Root, data);
    }

    private TreeNode AddInternal(TreeNode node, int data)
    {
        //base case
        if(node == null)
            node = new TreeNode(data);

        
        if(data == node.Value)
            return node;

        //recurse case
        if(data < node.Value)
        {
            node.Left = AddInternal(node.Left , data);
        }
        else
            node.Right = AddInternal(node.Right, data);

        return node;
    }

    public TreeNode Search(int key)
    {
        var queue = new Queue<TreeNode>();

        queue.Enqueue(Root);

        while(queue.Count > 0)
        {
            var node = queue.Dequeue();

            if(node.Value == key)
                return node;

            if(node.Left != null)
                queue.Enqueue(node.Left);

            if(node.Right != null)
                queue.Enqueue(node.Right);
            
        }

        return null;
    }

    //just converted from BinaryTree to BinarySearchSearch
    //below implementation can be improved by finding the left most node until Left=null
    //to get the lowest value node
    public TreeNode MinValue()
    {
        TreeNode minNode = null;
        int min = int.MaxValue;

        var stack = new Stack<TreeNode>();

        //DFS pre-order

        stack.Push(Root);

        while(stack.Count > 0)
        {
            var node = stack.Pop();

            if(node.Value < min)
            {
                min = node.Value;
                minNode = node;
            }

            if(node.Left != null)
                stack.Push(node.Left);

            if(node.Right != null)
                stack.Push(node.Right);
        }

        return minNode;

    }

    public int Depth()
    {
        int leftDepth = 0;
        int rightDepth = 0;
        return DepthInternalRecurse(Root, leftDepth, rightDepth);
    }

    public int DepthInternalRecurse(TreeNode node, int leftDepth, int rightDepth)
    {
        if(node == null)
            return 0;

        leftDepth = 1 + DepthInternalRecurse(node.Left, leftDepth, rightDepth);

        rightDepth = 1 + DepthInternalRecurse(node.Right, leftDepth, rightDepth);

        if( leftDepth >= rightDepth)
            return leftDepth;
        else
            return rightDepth;
    }

    public int Count()
    {
        int count = 0;
        var queue = new Queue<TreeNode>();

        queue.Enqueue(Root);

        while(queue.Count > 0)
        {
            var node = queue.Dequeue();

            count++;
            
            if(node.Left != null)
                queue.Enqueue(node.Left);

            if(node.Right != null)
                queue.Enqueue(node.Right);

        }

        return count;
    }
    
    public bool IsBST()
    {
       // return IsBSTInternal1(Root, false);

       return IsBSTInternal(Root, Root.Value, int.MaxValue);
    }

    //solution from Inernet
    private bool IsBSTInternal(TreeNode node, int min, int max)
    {
        if(node == null)
            return true;

        if( !(node.Value >= min && node.Value <= max))
            return false;

        return IsBSTInternal(node.Left, int.MinValue, node.Value) && IsBSTInternal(node.Right, node.Value, int.MaxValue );
    }

    // my own solution
    private bool IsBSTInternal1(TreeNode node, bool isbst)
    {
        //do DFS
        if(node == null)
            return true;


        Func<int,int,bool> LeftRangeChecker = (parentValue, nodeValue) => {
            if(nodeValue >= int.MinValue && nodeValue <= parentValue)
                return true;

            return false;
        };

        Func<int,int,bool> RightRangeChecker = (parentValue, nodeValue) => {
            if(nodeValue >= parentValue && nodeValue <= int.MaxValue)
                return true;

            return false;
        };


        if(node.Left != null)
        {
            if(!LeftRangeChecker(node.Value, node.Left.Value))
            {
                isbst = false;
                return isbst;
            }
                

            isbst = true;
            
            IsBSTInternal1(node.Left, isbst);
        }

        if(isbst == false)
            return false;

        if(node.Right != null)
        {
            if(!RightRangeChecker(node.Value, node.Right.Value))
            {
                isbst = false;
                return isbst;
            }

            isbst = true;
            IsBSTInternal1(node.Right, isbst);
        }

        return isbst;
    }

}

public class TreeNode
{
    public TreeNode(int value)
    {
        Value = value;
    }
    public int Value { get; set; }
    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }
}

// public class DFSTraversal
// {
//     List<string> result = new List<string>();

//     public string[] DFS(Node<string> node, List<string> result)
//     {
//         if(node == null)
//         {
//             return result.ToArray();
//         }

        

//         if(node.Left != null)
//             DFS(node.Left , result);
//         //to serialize to array, tree has to be a full tree. check if right has node then Left must be null
//         else if(node.Left == null && node.Right != null)
//             result.Add(null);
     
        
        
//         if(node.Right != null)
//             DFS(node.Right , result);
//         //to serialize to array, tree has to be a full tree. check if Left has node then Right must be null
//         else if(node.Right == null && node.Left != null)
//             result.Add(null);

//         if(node != null)
//             result.Add(node.Value);

//         return result.ToArray();

//     }
// }



// public class InPrePostTraversal
// {
//     public int[] InOrder(Node<int> node)
//     {
//         var result = new List<int>();
//         return InOrderInternal(node, result);
//     }

//     // left, root right
//     private int[] InOrderInternal(Node<int> node, List<int> result)
//     {   
//         if(node == null)
//             return result.ToArray();

//         if(node.Left != null)
//             InOrderInternal(node.Left, result);

//         result.Add(node.Value);

//         if(node.Right != null) 
//             InOrderInternal(node.Right, result);

//         return result.ToArray();
//     }

//     public int[] PreOrder(Node<int> node)
//     {
//         var r = new List<int>();
//         return PreOrderInternal(node, r);
//     }

//     //root left right
//     private int[] PreOrderInternal(Node<int> node, List<int> result)
//     {
//         if(node == null)
//             return result.ToArray();

//         result.Add(node.Value);

//         if(node.Left != null)
//             PreOrderInternal(node.Left, result);

//         if(node.Right != null)
//             PreOrderInternal(node.Right, result);

//         return result.ToArray();
//     }

//     public int[] PostOrder(Node<int> node)
//     {
//         var r = new List<int>();
//         return PostOrderInternal(node, r);
//     }

//     //left right root
//     private int[] PostOrderInternal(Node<int> node,  List<int> result)
//     {
//         if(node == null)
//             return result.ToArray();

//         if(node.Left != null)
//             PostOrderInternal(node.Left, result);

//         if(node.Right != null)
//             PostOrderInternal(node.Right, result);

//         result.Add(node.Value);
        
//         return result.ToArray();
//     }
// }

