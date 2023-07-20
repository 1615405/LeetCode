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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int len = 0;
        for (auto p = head; p; p = p->next) {
            len++;
        }
        ListNode* dummy = new ListNode(-1, head);
        ListNode* p0 = dummy;
        while (len >= k) {
            len -= k;
            ListNode* p0_remain = p0->next;

            ListNode* pre = p0;
            ListNode* cur = p0->next;
            for (int i = 1; i <= k; i++) {
                ListNode* cur_next = cur->next;
                cur->next = pre;
                pre = cur;
                cur = cur_next;
            }

            p0->next->next = cur;
            p0->next = pre;

            p0 = p0_remain;
        }

        return dummy->next;
    }
};