# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def isSameTree(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if(p.val != q.val):
                return False
            return isSameTree(p.left,q.right) and isSameTree(p.right,q.left)     
        return isSameTree(root.left,root.right)

#给定一个二叉树，检查它是否是镜像对称的。
#
# 
#
#例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#    1
#   / \
#  2   2
# / \ / \
#3  4 4  3
# 
#
#但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#   1
#   / \
#  2   2
#   \   \
#   3    3