namespace BinarySearchTree;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var bst = new BinarySearchTree();
        bst.Add(50);
        bst.Add(45);
        bst.Add(34);
        bst.Add(20);
        bst.Add(47);

        bst.Add(67);
        bst.Add(65);
        bst.Add(75);
        bst.Add(67);
        bst.Add(81);

        var smallestNode = bst.FindSmallest(bst.Root);
        var largestNode = bst.FindLargest(bst.Root);
    }

}

public class BinarySearchTree
{
    public TreeNode Root { get; set; }

    public void Add(int value)
    {
        if(Root == null)
        {
            Root = new TreeNode(value);
            return;
        }

        AddInternal(Root, value);
    }
    private void AddInternal(TreeNode node, int value)
    {
        if(node == null)
            return;

        if(value < node.Data)
        {
            if(node.Left == null)
            {
                node.Left = new TreeNode(value);
                return;
            }

            AddInternal(node.Left, value);
        }
        else
        {
            if(node.Right == null)
            {
                node.Right = new TreeNode(value);
                return;
            }

            AddInternal(node.Right, value);
        }
    }

    public void Remove(int data)
    {

    }

    public string PreorderTraversal(int data)
    {
        return "";
    }

    public string InorderTraversal(int data)
    {
        return "";
    }

    public string PostorderTraversal(int data)
    {
        return "";
    }

    public TreeNode FindSmallest(TreeNode node)
    {
        if(node.Left == null)
            return node;           

        return FindSmallest(node.Left);;
    }

    public TreeNode FindLargest(TreeNode node)
    {
        if(node.Right == null)
            return node;

        return FindLargest(node.Right);
    }

    public bool SearchNode(int data)
    {
        return false;
    }

    public TreeNode GetSuccessor(TreeNode node)
    {
        return null;
    }
}


public class TreeNode
{
    public TreeNode(int data)
    {
        Data = data;
    }
    public int Data { get; set; }

    public TreeNode Left { get; set; }
    public TreeNode Right { get; set; }
}

