"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            stack.extend(node.children[::-1])
            res.append(node.val)
        return res


# 给定一个 N 叉树，返回其节点值的前序遍历。
# 例如，给定一个 3叉树 :
# 返回其前序遍历: [1,3,5,6,2,4]。
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?

# 链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal