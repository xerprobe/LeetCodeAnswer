class Solution:
    def longestPalindrome(self, s: str) -> str:
        tranStr = '#'
        if(len(s) < 1):
            return ''
        for i in s:
            tranStr = tranStr + i + '#'
        radius = [0 for _ in tranStr]
        R = -1 #边界点
        c = -1 #中心点
        maxRadius = 0
        maxCenter = 0
        for i in range(len(tranStr)):
            radius[i] = 1 if R < i else min(radius[c*2 - i],R-i+1)
            while(i+radius[i]<len(tranStr) and i-radius[i]>-1):
                if(tranStr[i+radius[i]] == tranStr[i-radius[i]]):
                    radius[i] = radius[i] + 1
                else:
                    break
            if(i+radius[i]>R):
                R = i + radius[i] - 1
                c = i
            if(radius[i] > maxRadius):
                maxRadius = radius[i]
                maxCenter = i
        if(maxCenter%2):
            maxCenter = maxCenter // 2
            maxRadius = maxRadius // 2
            return s[maxCenter - maxRadius + 1 : maxCenter+maxRadius]
        else:
            maxCenter = maxCenter // 2
            maxRadius = maxRadius // 2
            return s[maxCenter - maxRadius:maxCenter+maxRadius]
            
'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''