namespace Merged2SortedLinkedList;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        var solution = new Solution();

        var list1 = new ListNode(5);
        //solution.AddToLastNode(list1, new ListNode(0));
        //solution.AddToLastNode(list1, new ListNode(4));

        var list2 = new ListNode(1);
        solution.AddToLastNode(list2, new ListNode(2));
        solution.AddToLastNode(list2, new ListNode(4));
        solution.AddToLastNode(list2, new ListNode(4));
        
        var merged = solution.MergeTwoLists(list1, list2);
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

    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        
        var result =  Merge(list1, list2, new ListNode(-1));

        //remove head node which is empty list
        if(result != null) {
            var temp = result.next;
            result = temp;
        }
        
        
        var current = result;
        while (current != null) {
            Console.WriteLine(current.val);
            current = current.next;
        }
        
        return result;
        
    }
    
    private ListNode Merge(ListNode list1, ListNode list2, ListNode result)
    {    
        
        if (list1 == null && list2 == null)
                return result;
        
        if (list1 != null && list2 != null) {
            
            if(list1.val == list2.val) {
                AddToLastNode(result, new ListNode(list1.val));
                AddToLastNode(result, new ListNode(list2.val));

                return Merge(list1.next ?? null, list2.next ?? null, result);
            }

            if(list1.val < list2.val) {
                
                AddToLastNode(result, new ListNode(list1.val));
                //AddToLastNode(result, new ListNode(list2.val));
                
                return Merge(list1.next ?? null, list2 ?? null, result);
            }
            
            if(list1.val > list2.val) {
                
                AddToLastNode(result, new ListNode(list2.val));
                //AddToLastNode(result, new ListNode(list1.val));
                
                return Merge(list1 ?? null, list2.next ?? null, result);
            }           
        }

        if(list1 == null && list2 != null)
        {
            // if(IsResultNodeEmpty(result))
            //     return list2;

            AddToLastNode(result, list2);
        }   

        if(list1 != null && list2 == null)
        {
            // if(IsResultNodeEmpty(result))
            //     return list1;

             AddToLastNode(result, list1);
        } 

        return result;
    }
    
    public ListNode AddToLastNode(ListNode node, ListNode toAdd)
    {
        if(toAdd == null)
            return node;

        //if result node already "fast forward to last node, add directly
        if(node.next == null) {
            node.next = toAdd;
            return node;
        }

        
        var current = node;

        while(current.next != null) {
            current = current.next;
        } //break when reach last node

        //last node of result
        current.next = toAdd;

        return current;
    }
    
    private string WriteResult(ListNode node)
    {
        string result = "";
        var current = node;
        while (current != null) {
            result += $", {current.val}";
            current = current.next;
        }
        return result;
    }
    
    private bool IsResultNodeEmpty(ListNode node)
    {
        if(node.val == -1)
            return true;

        return false;
    }
        
 }
}