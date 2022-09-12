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

        //BFS
        // if(root == null)
        //     return "";

        // var result = new List<string>();

        // _queue.Enqueue(root);

        // while(_queue.Count > 0)
        // {
        //     var currentNode = _queue.Dequeue();

        //     if(currentNode == null)
        //     {
        //         result.Add("null");
        //         continue;
        //     }
        //     else
        //         result.Add(currentNode.val.ToString());

        //     if(currentNode.left != null)
        //         _queue.Enqueue(currentNode.left);
        //     else
        //          _queue.Enqueue(null);

        //     if(currentNode.right != null)
        //         _queue.Enqueue(currentNode.right);
        //     else
        //          _queue.Enqueue(null);
        // }

        // return string.Join(",", result);
        
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

        //treeArr = treeArr.Where(x => x != "null").ToArray(); //no null 

        // var nodemap = new Hashtable(); // node value to node, where node value is use to look up node

        // foreach(string x in treeArr)
        // {
        //     if(x != "null")
        //         nodemap[x] = null; //new TreeNode(Convert.ToInt32(x));
        // }

        // //formula to find parent = MAth.Floor((arr-index - 1) / 2)

        // for(int i = 0; i < treeArr.Length; i++)
        // {
        //     if(treeArr[i] == "null")
        //         continue;

        //     var currentNodeValue = Convert.ToInt32(treeArr[i]);  //value is the key to node-map

        //     if(nodemap[currentNodeValue] == null)
        //         nodemap[currentNodeValue] = new TreeNode(currentNodeValue);

        //     int parentIndex = (i - 1 ) / 2;

        //     int valueOfParent = Convert.ToInt32(treeArr[parentIndex]);
        //     if(nodemap[valueOfParent] == null)
        //         nodemap[valueOfParent] = new TreeNode(valueOfParent);
            
        //     var parentNode = (TreeNode) nodemap[valueOfParent];

        //     if(currentNodeValue != valueOfParent)
        //     {
        //         var currentNode = (TreeNode)nodemap[currentNodeValue];
        //         if(parentNode.left == null)
        //             parentNode.left = currentNode;
        //         else
        //             parentNode.right = currentNode;
        //     }
        // }

        // int firstNodeValue = Convert.ToInt32(treeArr[0]);

        // var root = (TreeNode)nodemap[firstNodeValue];

        // return root;

        //return deserializeRecursive(treeArr, 0);
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

        // if(nodeArrIndex < arr.Length)
        // {
        //     var nodeVal = arr[nodeArrIndex];

        //     if(nodeVal == "null")
        //         return null;    //return null as node

        //     int nodeValue = Convert.ToInt32(arr[nodeArrIndex]);

        //     node = new TreeNode(nodeValue);

        //     node.left = deserializeRecursive(arr, (2 * nodeArrIndex) + 1);

        //     node.right = deserializeRecursive(arr, (2 * nodeArrIndex) + 2);

        // }
        
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));