from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        nodes = [root]
        index = 1
        flag = True
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
            if(flag):
                res.append(cache)
                flag = False
            else:
                res.append(cache[::-1])
                flag = True
        return res
'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
'''