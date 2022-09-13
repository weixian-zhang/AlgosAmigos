namespace Traversal_1;

public class UnitTest1
{
    [Fact]
    public void IsBST_True()
    {
        var a50 = new TreeNode(50);
        var a35 = new TreeNode(35);
        var a67 = new TreeNode(67);
        var a20 = new TreeNode(20);
        var a40 = new TreeNode(40);
        var a11 = new TreeNode(11);
        var a28 = new TreeNode(28);
        
        a50.Left = a35;
        a50.Right = a67;
        a35.Left = a20;
        a35.Right = a40;
        a40.Left = a28;

        var bt = new BinaryTree();
        bt.Root = a50;

        bool isItReallyBST = bt.IsBST();
    }

    [Fact]
    public void IsBST_False()
    {
        var a50 = new TreeNode(50);
        var a35 = new TreeNode(35);
        var a67 = new TreeNode(67);
        var a20 = new TreeNode(20);
        var a40 = new TreeNode(40);
        var a11 = new TreeNode(11);
        var a28 = new TreeNode(28);
        
        a50.Left = a35;
        a50.Right = a35; //a67;
        a35.Left = a20;
        a35.Right = a40;
        a40.Left = a28;

        var bt = new BinaryTree();
        bt.Root = a50;

        bool isItReallyBST = bt.IsBST();
    }

   
}

public class BinaryTree
{
    public TreeNode Root { get; set; }

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

