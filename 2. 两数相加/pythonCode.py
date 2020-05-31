# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = True
        firstNode = ListNode(0)
        nowNode = None
        while(l1!=None and l2!=None):
            if(flag):
                nowNode = ListNode(l1.val+l2.val)
                firstNode = nowNode
                flag = False
            else:
                nowNode.next = ListNode(l1.val+l2.val)
                nowNode = nowNode.next
            l1 = l1.next
            l2 = l2.next
        if(l1 != None):
            nowNode.next = l1
        if(l2 != None):
            nowNode.next = l2
        nowNode = firstNode
        while(nowNode != None):
            if(nowNode.val > 9):
                nowNode.val = nowNode.val % 10
                if(nowNode.next == None):
                    nowNode.next = ListNode(1)
                else:
                    nowNode.next.val = nowNode.next.val + 1
            nowNode = nowNode.next
        return firstNode

'''

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''