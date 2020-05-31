class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        ans = 1
        absn = abs(n)
        while(absn > 0):
            if(absn % 2):
                ans *= x
            x *= x
            absn = absn // 2
        return ans if(n > 0) else 1/ans
'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''