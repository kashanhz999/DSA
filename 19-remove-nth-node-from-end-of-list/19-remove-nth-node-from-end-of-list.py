# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        
        slow = dummy_head
        fast= dummy_head
        
        for i in range(n+1):
            fast = fast.next
        while fast !=None:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        
        return dummy_head.next
        
        