from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(ans: str, leftCount: int, rightCount: int):
            if(leftCount > n or rightCount > n):
                return
            if(leftCount == n and rightCount == n):
                result.append(ans)
            if(leftCount >= rightCount):
                generate(ans+'(',leftCount+1,rightCount)
                generate(ans+')',leftCount,rightCount+1)
        generate('',0,0)
        return result
'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''