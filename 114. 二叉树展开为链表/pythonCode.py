# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        head = TreeNode(None)
        preHead = head
        def perorder(root: TreeNode) -> None:
            if not root: return
            nonlocal head
            head.right = TreeNode(root.val)
            head = head.right
            perorder(root.left)
            perorder(root.right)
        perorder(root)
        root.left = None
        root.right = preHead.right.right

# 给定一个二叉树，原地将它展开为一个单链表。

#  

# 例如，给定二叉树

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# 将其展开为：

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
