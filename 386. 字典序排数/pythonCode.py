from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(target: int):
            if target > n:
                return
            res.append(target)
            for i in range(10):
                dfs(target*10+i)
        for i in range(1,10):
            dfs(i)
        return res


# 给定一个整数 n, 返回从 1 到 n 的字典顺序。

# 例如，

# 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。

# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。

# 链接：https://leetcode-cn.com/problems/lexicographical-numbers/