from typing import List
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = len(nums)*[1]
        step = len(nums)*[1]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if(dp[j] + 1 > dp[i]):
                        dp[i] = dp[j] + 1
                        step[i] = step[j]
                    elif(dp[j] + 1 == dp[i]):
                        step[i] += step[j]
        maxLength = max(dp)
        while maxLength in dp:
            index = dp.index(maxLength)
            dp.pop(index)
            res += step.pop(index)
        return res

# 给定一个未排序的整数数组，找到最长递增子序列的个数。

# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

# 链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence