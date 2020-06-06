# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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
        return res

'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
二叉树：[3,9,20,null,null,15,7]
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''