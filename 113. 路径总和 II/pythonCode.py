from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        def dfs(root: TreeNode, sum: int, nodes: List[int]):
            if not root: return
            sum -= root.val
            nodes = nodes+[root.val]
            if(sum == 0 and root.left == None and root.right == None):
                res.append(nodes)
            else:
                dfs(root.left,sum,nodes)
                dfs(root.right,sum,nodes)
        dfs(root,sum,[])
        return res

#给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
#
#说明: 叶子节点是指没有子节点的节点。
#
#示例:
#给定如下二叉树，以及目标和 sum = 22，
#
#              5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \    / \
#        7    2  5   1
#返回:
#
# [
#   [5,4,11,2],
#   [5,8,4,5]
#]
