# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        反转结束后，从原来的链表上看
            pre 指向反转这一段的末尾
            cur 指向反转这一段后续的下一个结点
        '''
        dummy = ListNode(next=head)
        p0 = dummy

        for _ in range(left - 1):
            p0 = p0.next
        
        pre = p0
        cur = p0.next
        for _ in range(right - left + 1):
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        

        p0.next.next = cur
        p0.next = pre

        return dummy.next



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode* dummy = new ListNode(-1, head);
        ListNode* p0 = dummy;

        for (int i = 1; i <= left - 1; i++) {
            p0 = p0->next;
        }

        ListNode* pre = p0;
        ListNode* cur = p0->next;

        for (int i = 1; i <= right - left + 1; i++) {
            ListNode* cur_next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = cur_next;
        }

        p0->next->next = cur;
        p0->next = pre;

        return dummy->next;
    }
};