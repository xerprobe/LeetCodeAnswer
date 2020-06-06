from typing import List
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 : return 0
        # 桶算法
        #第一步，算出最大值，最小值
        minVal,maxVal,n = float('inf'),float('-inf'),len(nums)
        for i in range(n):
            minVal = min(minVal,nums[i])
            maxVal = max(maxVal,nums[i])
        if minVal == maxVal:
            return 0
        #第二步，构建空间和给桶内赋值
        mins = (n+1)*[0]
        maxs = (n+1)*[0]
        has_num = (n+1)*[False]
        for num in nums:
            index = int((num - minVal) * n / (maxVal - minVal))
            maxs[index] = max(maxs[index],num) if has_num[index] else num
            mins[index] = min(mins[index],num) if has_num[index] else num
            has_num[index] = True
        #第三步，计算桶间最大差值，后一个桶的min减去前一个桶的max，返回结果
        res = 0
        preMax = maxs[0]
        for i in range(1, n+1):
            if has_num[i]:
                res = max(res,mins[i] - preMax)
                preMax = maxs[i]
        return res


# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
# 如果数组元素个数小于 2，则返回 0。

# 示例 1:
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。

# 示例 2:
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
# 说明:

# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

# 链接：https://leetcode-cn.com/problems/maximum-gap/