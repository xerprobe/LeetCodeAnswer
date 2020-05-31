class Solution:
    def convert(self, s: str, numRows: int) -> str:
        slen = len(s)
        result = ''
        temps = []
        if(slen == 0 or numRows < 1): return result
        if(numRows == 1): return s
        for i in range(slen):
            temp = ['' for _ in range(numRows)]
            group = i // (numRows - 1)
            cur = i % (numRows - 1)
            if(group % 2): temp[numRows - cur - 1] = s[i]
            else: temp[cur] = s[i]
            temps.append(temp)
        for j in range(numRows):
            for i in range(len(temps)):
                result = result + temps[i][j]
        return result
'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G
'''