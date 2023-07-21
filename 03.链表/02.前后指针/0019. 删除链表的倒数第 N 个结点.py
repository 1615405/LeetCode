# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        right = dummy
        for _ in range(n):
            right = right.next
        left = dummy
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* left = dummy;
        ListNode* right = dummy;
        while (n--) {
            right = right->next;
        }
        while (right->next) {
            left = left->next;
            right = right->next;
        }
        auto bin = left->next;
        left->next = left->next->next;
        delete(bin);
        return dummy->next;
    }
};