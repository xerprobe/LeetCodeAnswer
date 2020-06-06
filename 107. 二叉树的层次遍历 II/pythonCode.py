from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        nodes = [root]
        index = 1
        while(nodes):
            cache = []
            length = 0
            while(index):
                node = nodes.pop(0)
                cache.append(node.val)
                if(node.left):
                    nodes.append(node.left)
                    length += 1
                if(node.right):
                    nodes.append(node.right)
                    length += 1
                index -= 1
            index += length
            res.append(cache)
        return res[::-1]
'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
'''