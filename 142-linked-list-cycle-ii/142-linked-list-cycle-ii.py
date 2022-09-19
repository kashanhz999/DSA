# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        tmp_head = ListNode()
        tmp_head = head
        
        if tmp_head == None or tmp_head.next == None:
            return None
        
        fast, slow, entry = head, head, head
        while(fast.next and fast.next.next ):
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                while(slow != entry):
                    slow = slow.next
                    entry = entry.next
                return slow
        return None
            
        