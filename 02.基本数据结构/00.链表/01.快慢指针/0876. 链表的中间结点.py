# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowRunner = head
        fastRunner = head
        while fastRunner and fastRunner.next:
            slowRunner = slowRunner.next
            fastRunner = fastRunner.next.next
        return slowRunner



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
    ListNode* middleNode(ListNode* head) {
        ListNode* slowRunner = head;
        ListNode* fastRunner = head;
        while (fastRunner && fastRunner->next) {
            slowRunner = slowRunner->next;
            fastRunner = fastRunner->next->next;
        }
        return slowRunner;
    }
};