class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for index, i in enumerate(s):
            if count[i] == 1:
                return index
        return -1

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 示例：

# s = "leetcode"
# 返回 0

# s = "loveleetcode"
# 返回 2
#  
# 提示：你可以假定该字符串只包含小写字母。

# 链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string