class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t: return 0
        w = len(s)
        h = len(t)
        res = [w*[0] for _ in range(h)]
        for j in range(w):
            if(t[0] == s[j]):
                res[0][j] = 1
        for i in range(1,h):
            count = 0
            for j in range(i,w - h + i + 1):
                if(t[i] == s[j]):
                    res[i][j] += count
                count += res[i-1][j]
        return sum(res[-1])

# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

# 题目数据保证答案符合 32 位带符号整数范围。

#  

# 示例 1：

# 输入：S = "rabbbit", T = "rabbit"
# 输出：3
# 解释：

# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2：

# 输入：S = "babgbag", T = "bag"
# 输出：5
# 解释：

# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
# (上箭头符号 ^ 表示选取的字母)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
