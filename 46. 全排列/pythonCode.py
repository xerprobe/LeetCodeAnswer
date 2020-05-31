from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if(len(nums)<=1):
            return [nums]
        for i in range(len(nums)):
            other = nums[0:i]
            other.extend(nums[i+1:])
            out = self.permute(other)
            for r in out:
                r.append(nums[i])
            result.extend(out)
        return result
'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''