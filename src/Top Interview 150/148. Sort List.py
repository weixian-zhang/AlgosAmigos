from typing import Optional, List
from copy import deepcopy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # using extra space to add Linked List values in List, sort and create new Linked List
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodeList = []

        curr = head

        while curr:
            nodeList.append(curr.val)
            curr = curr.next
        
        nodeList.sort()

        dummy = ListNode()
        curr = dummy

        for x in nodeList:
            curr.next = ListNode(x)
            curr = curr.next

        return dummy.next
    

    # use merge sort O(n log n)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # head.next indicates single node
        if not head or not head.next:
            return head

        def total_nodes(node: ListNode) -> int:
            total = 0

            curr = node

            while curr:
                total += 1
                curr = curr.next
            
            return total
        

        def to_node(node: ListNode, start: int, end: int):

            curr = node
            count = 0

            # navigate to start node first
            while count != start:
                count += 1
                curr = curr.next

            startNode = curr
            curr = startNode
            count = start

            while curr:

                if count == end:
                    curr.next = None
                    return startNode
                else:
                    count += 1
                    curr = curr.next
            
            return startNode
        
        def get_mid(node: ListNode):

            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def _merge(left: ListNode, right: ListNode) -> ListNode:

            dummy = ListNode()

            currDummy = dummy
            currLeft, currRight = left, right
            
            while currLeft and currRight:

                if currLeft.val < currRight.val:
                    currDummy.next = ListNode(currLeft.val)
                    currLeft = currLeft.next
                    currDummy = currDummy.next
                elif currLeft.val > currRight.val:
                    currDummy.next = ListNode(currRight.val)
                    currRight = currRight.next
                    currDummy = currDummy.next

                # values are equal
                else:
                    currDummy.next = ListNode(currLeft.val)
                    currDummy = currDummy.next

                    currDummy.next = ListNode(currRight.val)
                    currDummy = currDummy.next

                    currLeft = currLeft.next
                    currRight = currRight.next

            while currLeft:
                currDummy.next = ListNode(currLeft.val)
                currLeft = currLeft.next
                currDummy = currDummy.next

            while currRight:
                currDummy.next = ListNode(currRight.val)
                currRight = currRight.next
                currDummy = currDummy.next

            return dummy.next



        def _merge_sort(node: ListNode) -> ListNode:
            
            # base case
            if not node or not node.next:
                return node

            # recursive case/step
            # total = total_nodes(node)

            # midIdx = total // 2

            left = node #to_node(deepcopy(node), 0, midIdx - 1)

            # same linked list without deepcopy, split into 2 halves
            right = get_mid(node) #to_node(deepcopy(node), midIdx, total - 1)
            tempRight = right.next
            right.next = None
            right = tempRight

            left = _merge_sort(left)

            right = _merge_sort(right)

            merged = _merge(left, right)

            return merged


        sortedNode = _merge_sort(head)

        return sortedNode





s = Solution()

n4 = ListNode(4)
n3 = ListNode(3)
n1 = ListNode(1)
n2 = ListNode(2)
n4.next = n2
n2.next = n1
n1.next = n3

[4,19,14,5,-3,1,8,5,11,15]

# n4 = ListNode(4)
# n19 = ListNode(19)
# n14 = ListNode(14)
# n5_1 = ListNode(5)
# n5_2 = ListNode(5)
# nMinus3 = ListNode(-3)
# n1 = ListNode(1)
# n8 = ListNode(8)
# n5 = ListNode(5)
# n11 = ListNode(11)
# n15 = ListNode(15)

# n4.next = n19
# n19.next = n14
# n14.next = n5_1
# n5_1.next = nMinus3
# nMinus3.next = n1
# n1.next = n8
# n8.next = n5_2
# n5_2.next = n11
# n11.next = n15

s.sortList(n4)









s.sortList(n4)