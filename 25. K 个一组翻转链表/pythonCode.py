# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if(k == 1): return head
        firstNode = head
        head = ListNode(None)
        head.next = firstNode
        secondNode = head
        firstNode = head
        beforeNode = head
        listLen = 0
        while(secondNode.next!=None):
            listLen += 1
            secondNode = secondNode.next
        secondNode = firstNode.next
        for _ in range(listLen // k):
            lastNode = secondNode
            for _ in range(k):
                lastNode = lastNode.next
            for _ in range(k):
                firstNode = secondNode
                secondNode = secondNode.next
                firstNode.next = lastNode
                lastNode = firstNode
            beforeNode.next = firstNode
            for _ in range(k):
                beforeNode = beforeNode.next
            firstNode = beforeNode
        return head.next
'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5
'''