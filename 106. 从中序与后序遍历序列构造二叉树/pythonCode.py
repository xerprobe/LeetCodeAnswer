from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder:
            pos = inorder.index(postorder[-1])
            node = TreeNode(inorder[pos])
            node.left = self.buildTree(inorder[:pos],postorder[:pos])
            node.right = self.buildTree(inorder[pos+1:],postorder[pos:-1])
            return node
        else:
            return None
'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：
'''
#    3
#   / \
#  9  20
#    /  \
#   15   7
