class Solution:
    def trailingZeroes(self, n: int) -> int:
        d = 0
        res = 0
        while(5**d < n):
            d += 1
        while(d):
            res += n // 5**d
            d -= 1
        return res

# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 示例 1:
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。

# 示例 2:
# 输入: 5
# 输出: 1

# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。

# 链接：https://leetcode-cn.com/problems/factorial-trailing-zeroes