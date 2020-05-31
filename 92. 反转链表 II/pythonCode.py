# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if(m == n): return head
        first = ListNode(None)
        first.next = head
        head = first
        second = head
        for _ in range(m-1):
            second = second.next
        first = second.next.next
        pos = second.next
        for _ in range(n-m):
            temp = first.next
            first.next = pos
            pos = first
            first = temp
        second.next.next = first
        second.next = pos
        return head.next
'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''