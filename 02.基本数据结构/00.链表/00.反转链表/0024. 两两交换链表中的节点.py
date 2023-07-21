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
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(-1, head);
        ListNode* p0 = dummy;

        while (p0->next && p0->next->next) {
            ListNode* one = p0->next;
            ListNode* two = p0->next->next;

            p0->next = two;
            one->next = two->next;
            two->next = one;

            p0 = one;
        }

        return dummy->next;
    }
};