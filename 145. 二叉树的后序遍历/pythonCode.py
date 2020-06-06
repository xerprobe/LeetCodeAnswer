from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        pre = root
        stack = [root]
        while(stack):
            node = stack[-1]
            if (not node.right and not node.left) or pre == node.right or pre == node.left:
                pre = stack.pop(-1)
                res.append(pre.val)    
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
# 给定一个二叉树，返回它的 后序 遍历。

# 示例:

# 输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 

# 输出: [3,2,1]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal