class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        s = s[::-1]
        if(x < 0): x = -int(s)
        else: x = int(s)
        if(x >= 2147483648 or x <-2147483648):
            return 0
        else:
            return x
'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
'''