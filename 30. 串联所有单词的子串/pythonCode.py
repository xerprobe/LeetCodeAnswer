from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0:
            return []
        if len(words) == 0:
            return []
        wordsLen = len(words[0])
        childListLen = len(words) * wordsLen
        checkDic = dict()
        flag = True
        for word in words:
            if word in checkDic.keys():
                checkDic[word] += 1
            else:
                checkDic[word] = 1
        
        wordsDic = dict(zip(words,[0]*len(words)))
        res = []
        for i in range(0,len(s) - childListLen + 1):
            for j in range(i,i+childListLen,wordsLen):
                word = s[j:j+wordsLen]
                if word in words:
                    wordsDic[word] += 1
                else:
                    flag = False
                    break
            if flag:
                for key in checkDic.keys():
                    if checkDic[key] != wordsDic[key]:
                        flag = False
                        break
                if flag:
                    res.append(i)
            for key in wordsDic.keys():
                wordsDic[key] = 0
            flag = True
        return res


# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

# 示例 1：

# 输入：
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。

# 示例 2：

# 输入：
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# 输出：[]

# 链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words