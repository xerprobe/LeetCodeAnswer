# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

def guess(num: int) -> int:
    pick = 50
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        g = n
        res = guess(n)
        while res:
            if res == 1:
                n = (g + n) // 2
            elif res == -1:
                g = n
                n = n // 2
            res = guess(n)
        return n

# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

# -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！
 

# 示例 :

# 输入: n = 10, pick = 6
# 输出: 6

# 链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower/
