# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy

        while p0.next and p0.next.next:
            one = p0.next
            two = p0.next.next

            p0.next = two
            one.next = two.next
            two.next = one
            
            p0 = one
        
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur_next = head.next
        head.next = self.swapPairs(cur_next.next)
        cur_next.next = head
        return cur_next