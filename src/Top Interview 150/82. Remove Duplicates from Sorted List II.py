# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    # standard solution - 2 pointers, curr/head pointer skip duplicates and use prev.next to point to next
    # unique node
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head

        while curr.next:

            if curr.next and curr.val != curr.next.val:
                prev = curr
                curr = curr.next
            else:

                while curr.next and curr.val == curr.next.val:
                    curr = curr.next

                prev.next = curr.next

                curr = curr.next

        return dummy.next


    # my solution using list to re-create LinkedList
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
        
    #     dummy = ListNode(-1)
    #     curr_dummy = dummy
    #     dupTracker = set()
    #     nodeToDel = []

    #     curr = head

    #     while curr:
    #         if curr.val not in dupTracker:
    #             dupTracker.add(curr.val)
    #         else:
    #             if curr.val not in nodeToDel:
    #                 nodeToDel.append(curr.val)
            
    #         curr = curr.next

    #     nodesToCreate = [x for x in list(dupTracker) if x not in nodeToDel]

    #     nodesToCreate.sort()

    #     for x in nodesToCreate:
    #         curr_dummy.next = ListNode(x)
    #         curr_dummy = curr_dummy.next

    #     return dummy.next



#-3,-1,-1,0,0,0,0,0,2]
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
#l1 = ListNode(-3, ListNode(-1, ListNode(-1, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(0, ListNode(2)))))))))
s = Solution()
s.deleteDuplicates(l1)