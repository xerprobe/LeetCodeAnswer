from typing import List
import bisect

class Solution:
    def dfs(self,nums: List[int],l: int, r: int):
        if r - l <= 1:
            return 0
        mid = (l+r)>>1
        res = self.dfs(nums,l,mid)+self.dfs(nums,mid,r)
        temp = sorted(nums[l:mid])
        for i in range(mid,r):
            res += mid - bisect.bisect_left(temp,nums[i]+0.1) - l
        return res
    def reversePairs(self, nums: List[int]) -> int:
        return self.dfs(nums,0,len(nums))

# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

# 示例 1:
# 输入: [7,5,6,4]
# 输出: 5

# 限制：
# 0 <= 数组长度 <= 50000

# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof