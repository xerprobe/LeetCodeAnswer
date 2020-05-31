class Solution:
    def addBinary(self, a: str, b: str) -> str:
        while(len(a) != len(b)):
            if(len(a) > len(b)):
                b = '0' + b
            else:
                a = '0' + a
        up = 0
        i = len(a) - 1
        result = ''
        while(i >= 0):
            s = str(int(int(a[i])^int(b[i])^up))
            if(int(a[i])+int(b[i])+up > 1):
                up = 1
            else:
                up = 0
            result = s + result
            i -= 1
        if(up == 1):
            result = '1' + result
        return result

'''
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
'''