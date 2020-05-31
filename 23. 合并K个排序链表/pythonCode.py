# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(len(lists) == 1):
            return lists[0]
        if(len(lists) == 0):
            return None
        if(len(lists) == 2):
            if(lists[0] == None or lists[0].val == None):
                return lists[1]
            elif(lists[1] == None or lists[1].val == None):
                return lists[0]
            return self.mergeTwoLists(lists[0],lists[1])
        return self.mergeTwoLists(self.mergeKLists(lists[1:]),lists[0])


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        cur = head
        while(l1 != None and l2 != None):
            if(l1.val < l2.val):
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if(l1 == None):
            cur.next = l2
        else:
            cur.next = l1
        return head.next
'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''