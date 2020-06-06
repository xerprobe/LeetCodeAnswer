from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightNode = dict()
        queue = deque([(root, 0)])
        maxDepth = -1
        while queue:
            node, depth = queue.popleft()
            if node:
                maxDepth = max(maxDepth,depth)
                rightNode[depth] = node.val
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        return [rightNode[depth] for depth in range(maxDepth + 1)]


# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

# 示例:
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:

#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

# 链接：https://leetcode-cn.com/problems/binary-tree-right-side-view