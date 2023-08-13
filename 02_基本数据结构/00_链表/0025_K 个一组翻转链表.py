# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        dummy = ListNode(next=head)
        p0 = dummy

        while n >= k:
            n -= k
            p0_remain = p0.next

            pre = p0
            cur = p0.next
            for _ in range(k):
                cur_next = cur.next
                cur.next = pre
                pre = cur
                cur = cur_next
            
            p0.next.next = cur
            p0.next = pre
            p0 = p0_remain
        
        return dummy.next