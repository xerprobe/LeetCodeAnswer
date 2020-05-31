from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        index = len(nums)
        if(index > 0):
            for i in range(1,len(nums)):
                if(nums[i] != nums[i-1]):
                    index = i
                    break
            result = self.subsetsWithDup(nums[index:])
            s = []
            for i in range(index):
                for j in result:
                    s.append(nums[i:index]+j)
            return s+result
        return [[]]
'''

给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''