# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        n = 0
        while cur:
            cur = cur.next
            n += 1
        
        mid = self.middleNode(head)
        if n % 2 == 1:
            mid = mid.next
        mid = self.reverseList(mid)
        while mid:
            if mid.val != head.val:
                return False
            mid = mid.next
            head = head.next
        return True