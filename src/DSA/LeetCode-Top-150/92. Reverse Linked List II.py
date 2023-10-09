class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        
        nums = self.linkedlist_to_list(head)
        
        leftIdx = left-1 #nums.index(left)
        
        rightIdx = right-1 # nums.index(right)
        
        while leftIdx <= rightIdx:
            nums[leftIdx], nums[rightIdx] = nums[rightIdx], nums[leftIdx]
            leftIdx += 1
            rightIdx -= 1
            
        node = self.list_to_linkedlist(nums)
        
        return node
    
    
    def linkedlist_to_list(self, head) -> list[int]:
        
        nums = []
        
        current = head

        while current is not None:
            nums.append(current.val)
            current = current.next
            
        return nums
            
            

    def list_to_linkedlist(self, nums: list[int]) -> ListNode:
        
        dummyNode = ListNode(-1)
        current = dummyNode
        
        for x in nums:
            current.next = ListNode(x)
            current = current.next
            
        return dummyNode.next
            
        
    
    
if __name__ == '__main__':
    
    s = Solution()
    
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l7 = ListNode(7)
    
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    l6.next = l7
    
    s.reverseBetween(l1, left=3, right=6)