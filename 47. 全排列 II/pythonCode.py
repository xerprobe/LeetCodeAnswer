from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        vis = len(nums)*[0]
        return self.permute(nums,vis)


    def permute(self, nums: List[int], vis: List[int]) -> List[List[int]]:
        result = []
        if(len(nums)<=1):
            return [nums]
        for i in range(len(nums)):
            if(i > 0 and nums[i-1] == nums[i] and vis[i-1] !=0):
                vis[i] = 1
                continue
            other = nums[0:i]
            other.extend(nums[i+1:])
            otherVis = vis[0:i]
            otherVis.extend(vis[i+1:])
            out = self.permute(other,otherVis)
            vis[i] = 1
            for r in out:
                r.append(nums[i])
            result.extend(out)
        return result
'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''