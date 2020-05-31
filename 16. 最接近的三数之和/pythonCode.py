from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        threeSum = nums[0] + nums[1] + nums[2]
        closeNum = abs(target - threeSum)
        result = threeSum
        for i in range(len(nums)-2):
            top = i + 1
            botten = len(nums) - 1   
            while(top < botten):
                threeSum = nums[i] + nums[top] + nums[botten]
                if(closeNum > abs(target - threeSum)):
                    closeNum = abs(target - threeSum)
                    result = threeSum
                if(threeSum > target):
                    botten -= 1
                elif(threeSum < target):
                    top += 1
                else:
                    return target
        return result
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''