# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 876. 链表的中间结点
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    # 206. 反转链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            cur_next = cur.next
            cur.next = pre
            pre = cur
            cur = cur_next
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)

        while head2.next:
            one_next = head.next
            two_next = head2.next

            head.next = head2
            head2.next = one_next

            head = one_next
            head2 = two_next



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
    void reorderList(ListNode* head) {
        function<ListNode*(ListNode*)> middleNode = [&](ListNode* head) -> ListNode* {
            ListNode* slow = head;
            ListNode* fast = head;
            while (fast && fast->next) {
                slow = slow->next;
                fast = fast->next->next;
            }
            return slow;
        };

        function<ListNode*(ListNode*)> reverseList = [&](ListNode* head) -> ListNode* {
            ListNode* pre = nullptr;
            ListNode* cur = head;
            while (cur) {
                ListNode* cur_next = cur->next;
                cur->next = pre;
                pre = cur;
                cur = cur_next;
            }
            return pre;
        };

        ListNode* mid = middleNode(head);
        ListNode* head2 = reverseList(mid);
        while (head2->next) {
            ListNode* one_next = head->next;
            ListNode* two_next = head2->next;

            head->next = head2;
            head2->next = one_next;

            head = one_next;
            head2 = two_next;
        }
    }
};