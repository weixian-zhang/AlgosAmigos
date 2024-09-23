using System.Collections;

namespace _297.SerializeDeserializeBinaryTree;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var root = new TreeNode(1);
        var two = new TreeNode(2);
        var three = new TreeNode(3);
        var four = new TreeNode(4);
        var five = new TreeNode(5);
        var six = new TreeNode(6);
        var seven = new TreeNode(7);

        root.left = two;
        root.right = three;
        three.left = four;
        three.right = five;
        // four.left = six;
        // four.right = seven;

        Codec ser = new Codec();
        Codec deser = new Codec();
        string r = ser.serialize(root);
        TreeNode node = deser.deserialize(r);
    }
}


 public class TreeNode {
     public int val;
     public TreeNode left;
     public TreeNode right;
     public TreeNode(int x) { val = x; }
 }

public class Codec {

    Queue<TreeNode> _queue = new Queue<TreeNode>();
    
    // Encodes a tree to a single string.
    public string serialize(TreeNode root) {

        return DFS(root);       
    }

    List<string> _result = new List<string>();
    private string DFS(TreeNode node)
    {
        if(node == null)
        {
            _result.Add("null");
            return null;
        }

        _result.Add(node.val.ToString());

        DFS(node.left);
        DFS(node.right);

        return string.Join(",", _result);
    }


    // Decodes your encoded data to tree.
    public TreeNode deserialize(string tree) {
        
        string[] treeArr = tree.Split(",");

        TreeNode root = deserializeRecursive(treeArr);

        return root;
    }

    private int nodeArrIndex = 0;
    private TreeNode deserializeRecursive(string[] arr)
    {
        if(nodeArrIndex >= arr.Length)
            return null;

        if(arr[nodeArrIndex] == "null")
        {
            return null;
        }

        int nodeValue = Convert.ToInt32(arr[nodeArrIndex]);

        TreeNode node = new TreeNode(nodeValue);

        nodeArrIndex++;

        node.left = deserializeRecursive(arr);

        nodeArrIndex++;

        node.right = deserializeRecursive(arr);
        
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));