import unittest


# max nodes in each list is 0, 50
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def to_list(self, l: ListNode):
            vals = []
    
            curr = l
    
            while curr:
                vals.append(curr.val)
                curr = curr.next
    
            return vals

    def mergeTwoLists(self, list1: ListNode, list2: ListNode):

        if not list1:
            return list2
        if not list2:
            return list1


        l1_curr = list1

        l2_curr = list2

        while l2_curr:

            if l2_curr.val < l1_curr.val:

                l2_next = l2_curr.next

                dummy = ListNode(l2_curr.val)
                dummy.next = l1_curr

                #l2_curr.next = l1_curr
                
                l1_curr = dummy

                # move l2 pointer
                l2_curr = l2_next

            elif l2_curr.val == l1_curr.val:
                l1_next = l1_curr.next

                l2_next = l2_curr.next

                l1_curr.next = l2_curr

                l2_curr.next = l1_next

                # move l1 pointer to current
                l1_curr = l1_curr.next

                # move l2 pointer to current
                l2_curr = l2_next
                
            else:
                while l2_curr.val > l1_curr.val and l1_curr.next and l2_curr.val > l1_curr.next.val:
                    l1_curr = l1_curr.next

                # detach rest of l1
                l1_next = l1_curr.next

                # detach rest of l2
                l2_next = l2_curr.next

                l1_curr.next = l2_curr

                l2_curr.next = l1_next

                l1_curr = l1_curr.next

                l2_curr = l2_next


        return list1



l1 = ListNode(2)
l2 = ListNode(1)
s = Solution()
print(s.to_list(s.mergeTwoLists(l1, l2)))


class TestSolution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solution = Solution()

    def to_list(self, l: ListNode):
        vals = []

        curr = l

        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals
    

    # 1,2,3
    # 4,5,6
    def test_1_2_3__4_5_6(self):

        l1 = ListNode(1, ListNode(2, ListNode(3)))

        l2 = ListNode(4, ListNode(5, ListNode(6)))

        r = self.solution.mergeTwoLists(l1, l2)

        vals = self.to_list(r)

        self.assertEqual(vals, [1,2,3,4,5,6])




    # 1,1,1
    # 2,3
    def test_1_1_1__2_3(self):

        l1 = ListNode(1, ListNode(1, ListNode(1)))

        l2 = ListNode(2, ListNode(3))

        self.solution.mergeTwoLists(l1, l2)

        r = self.solution.mergeTwoLists(l1, l2)
        vals = self.to_list(r)
        self.assertEqual(vals, [1,1,1,2,3])


    # 4, 8, 11
    # 6, 9


    # -1, -3, -5, -7
    # -10, -20

    # none
    # none

    # 3, 5
    # none

    # none
    # 50, 100

    # 50, 100
    # 1, 5, 10


