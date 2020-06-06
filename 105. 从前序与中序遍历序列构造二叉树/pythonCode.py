from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(order: List[int]) -> TreeNode:
            if preorder and preorder[0] in order:
                pos = order.index(preorder[0])
                node = TreeNode(preorder.pop(0))
                node.left = build(order[:pos])
                node.right = build(order[pos+1:])
                return node
            else:
                return None
        return build(inorder)

'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：
'''
#    3
#   / \
#  9  20
#    /  \
#   15   7
