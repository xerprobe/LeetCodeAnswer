class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.deepMatch(s,p,0,0)
    def deepMatch(self, s: str, p: str, sCur: int, pCur: int) -> bool:
        if(pCur >= len(p)):
            return sCur >= len(s)
        if(sCur >= len(s)):
            return self.lastIsStar(p,pCur)
        if (len(p) - pCur > 1 and p[pCur + 1] != '*') or len(p) - pCur == 1 :
            if not self.matchChar(s[sCur],p[pCur]):
                return False
            else:
                return self.deepMatch(s,p,sCur+1,pCur+1)
        else:
            if(self.deepMatch(s,p,sCur,pCur+2)):
                return True
            while(self.matchChar(s[sCur],p[pCur])):
                sCur = sCur + 1
                if(self.deepMatch(s,p,sCur,pCur+2)):
                    return True
                if(sCur >= len(s)):
                    return self.lastIsStar(p,pCur)
            return False
    def matchChar(self, s:str, p: str) -> bool:
        return s == p or p =='.'
    def lastIsStar(self, p: str, pCur: int) -> bool:
        while(pCur < len(p)):
            if(len(p) - pCur == 1 or p[pCur + 1] != '*'):
                return False
            pCur = pCur + 2
        return True
'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。

示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
'''