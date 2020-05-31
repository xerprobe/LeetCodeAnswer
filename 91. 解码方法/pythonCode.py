class Solution:
    def numDecodings(self, s: str) -> int:
        dp = (len(s)+1)*[0]
        dp[0] = 1
        if(s[0] == '0'): return 0
        for i in range(len(s)):
            dp[i+1] = 0 if(s[i] == '0') else dp[i]
            if(i>0 and int(s[i-1]+s[i]) <= 26 and int(s[i-1]+s[i]) > 9):
                dp[i+1] += dp[i-1]
        return dp[-1]
'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''