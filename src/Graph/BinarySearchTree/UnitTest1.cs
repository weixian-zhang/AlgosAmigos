namespace BinarySearchTree;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var bst = new BinarySearchTree();
        // bst.Add(1);
        // bst.Add(2);
        // bst.Add(20);
        // bst.Add(19);
        // bst.Add(3);
        // bst.Add(4);
        // bst.Add(18);
        // bst.Add(17);
        // bst.Add(5);
        // bst.Remove(3);
        // bst.Remove(18);

        bst.Add(0);
        bst.Add(-2);
        bst.Add(2);
        bst.Add(-4);
        bst.Add(-1);
        bst.Add(3);

        bst.Remove(-2);

        // var smallestNode = bst.FindSmallest(bst.Root);
        // var largestNode = bst.FindLargest(bst.Root);
    }

}

public class BinarySearchTree
{
    int  _nodeCount = 0;
    public TreeNode Root { get; set; }

    public void Add(int value)
    {
        if(Root == null)
        {
            Root = new TreeNode(value);
            _nodeCount++;
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
            //leftmost null is the smallest value
            if(node.Left == null)
            {
                node.Left = new TreeNode(value);
                _nodeCount++;
                return;
            }

            AddInternal(node.Left, value);
        }
        //right most null is the largest value
        else
        {
            if(node.Right == null)
            {
                node.Right = new TreeNode(value);
                _nodeCount++;
                return;
            }

            AddInternal(node.Right, value);
        }
    }

    public void Remove(int data)
    {
        RemoveInternal(Root, data);
    }

    public TreeNode RemoveInternal(TreeNode nodeToRemove, int value)
    {
        //node don't exist, value does not match any of node data
        if(nodeToRemove == null)
            return null;

        //find node to remove
        if(value == nodeToRemove.Data) //found node to remove
        {
            //leaf node with no children
            if(nodeToRemove.Left == null & nodeToRemove.Right == null)
            {
                nodeToRemove = null;
                return null;
            }
            //node with left child
            else if(nodeToRemove.Left != null & nodeToRemove.Right == null)
            {
                //replace with left child
                TreeNode leftChild = nodeToRemove.Left;
                nodeToRemove = null;
                _nodeCount--;
                return leftChild;
            }
            //node with right child
            else if(nodeToRemove.Left == null & nodeToRemove.Right != null)
            {
                TreeNode rightChild = nodeToRemove.Right;
                nodeToRemove = null;
                _nodeCount--;
                return rightChild;
            }
            //node with both left and right children
            else if(nodeToRemove.Left != null & nodeToRemove.Right != null)
            {
                //find left subtree largest value, just preference
                //or also OK to find right subtree smallest

                TreeNode leftChild = nodeToRemove.Left;

                TreeNode largestNodeOfLeftSubTree = FindLargest(nodeToRemove);

                largestNodeOfLeftSubTree.Left = leftChild;  //retain original left child

                nodeToRemove = null;

                _nodeCount--;

                return largestNodeOfLeftSubTree;
                
            }
            
        }

        //dig into left tree as value is > node
        if(value < nodeToRemove.Data)
        {
            if(nodeToRemove.Left != null)
                nodeToRemove.Left = RemoveInternal(nodeToRemove.Left, value);
        }

        //dig into right tree as value is > node
        else
        {
            if(nodeToRemove.Right != null)
                nodeToRemove.Right = RemoveInternal(nodeToRemove.Right, value);
        }

        return nodeToRemove;
        
    }

    public int Size()
    {
        return _nodeCount;
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

