namespace _206.ReversedLinkedList;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var node1 = new ListNode(1);
        var node2 = new ListNode(2);
        var node3 = new ListNode(3);
        var node4 = new ListNode(4);
        var node5 = new ListNode(5);

        node1.next = node2;
        node2.next = node3;
        node3.next = node4;
        node4.next = node5;

        var s = new Solution();
        var r = s.ReverseList(node1);
    }
}


 public class ListNode {
      public int val;
      public ListNode next;
      public ListNode(int val=0, ListNode next=null) {
          this.val = val;
          this.next = next;
      }
  }

  

public class Solution {
    List<int> reverseList = new List<int>();

    public ListNode ReverseList(ListNode head) 
    {
        if(head == null)
            return head;

        //GetLinkedNodes(head);
        ListNode current = head;
        while(current != null)
        {
            reverseList.Add(current.val);
            current = current.next;
        }

        reverseList.Reverse();

        ListNode resultNode = null;

        foreach(var val in reverseList)
        {
            resultNode = InsertNode(resultNode, val);
        }

        return resultNode; 
    }

    //recursively
    private void GetLinkedNodes(ListNode node)
    {
        if(node == null)
            return;

        reverseList.Add(node.val);

        GetLinkedNodes(node.next);
    }

    public ListNode InsertNode(ListNode node, int val)
    {
        if(node == null)
        {
            node = new ListNode(val);
            return node;
        }

        
        ListNode current = node;

        while(current.next != null) //"next" is important, if not will end up on null node
        {
            current = current.next;
        }

        current.next = new ListNode(val);

        return node;
    }
}