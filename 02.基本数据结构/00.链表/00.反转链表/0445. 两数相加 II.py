# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  # 把下一个节点指向自己
        head.next = None  # 断开指向下一个节点的连接，保证最终链表的末尾节点的 next 是空节点
        return new_head

    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwo(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        carry += l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = carry % 10  # 每个节点保存一个数位
        l1.next = self.addTwo(l1.next, l2.next if l2 else None, carry // 10)  # 进位
        return l1

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)  # l1 和 l2 反转后，就变成【2. 两数相加】了
        l3 = self.addTwo(l1, l2)
        return self.reverseList(l3)




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
    ListNode *reverseList(ListNode *head) {
        if (head == nullptr || head->next == nullptr)
            return head;
        auto new_head = reverseList(head->next);
        head->next->next = head; // 把下一个节点指向自己
        head->next = nullptr; // 断开指向下一个节点的连接，保证最终链表的末尾节点的 next 是空节点
        return new_head;
    }

    // l1 和 l2 为当前遍历的节点，carry 为进位
    ListNode *addTwo(ListNode *l1, ListNode *l2, int carry = 0) {
        if (l1 == nullptr && l2 == nullptr) // 递归边界：l1 和 l2 都是空节点
            return carry ? new ListNode(carry) : nullptr; // 如果进位了，就额外创建一个节点
        if (l1 == nullptr) // 如果 l1 是空的，那么此时 l2 一定不是空节点
            swap(l1, l2); // 交换 l1 与 l2，保证 l1 非空，从而简化代码
        carry += l1->val + (l2 ? l2->val : 0); // 节点值和进位加在一起
        l1->val = carry % 10; // 每个节点保存一个数位
        l1->next = addTwo(l1->next, (l2 ? l2->next : nullptr), carry / 10); // 进位
        return l1;
    }

public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        l1 = reverseList(l1);
        l2 = reverseList(l2); // l1 和 l2 反转后，就变成【2. 两数相加】了
        auto l3 = addTwo(l1, l2);
        return reverseList(l3);
    }
};