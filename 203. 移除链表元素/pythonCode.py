# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = ListNode(None)
        pre.next = head
        head = pre
        while(head.next):
            if(head.next.val == val):
                head.next = head.next.next
            else:
                head = head.next
        return pre.next

# 删除链表中等于给定值 val 的所有节点。

# 示例:

# 输入: 1->2->6->3->4->5->6, val = 6
# 输出: 1->2->3->4->5

# 链接：https://leetcode-cn.com/problems/remove-linked-list-elements/