from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if(len(nums) < 4): return []
        result = []
        nums = sorted(nums)
        lastTwoSum = nums[-1] + nums[-2]
        lastThreeSum = lastTwoSum + nums[-3]
        for i in range(len(nums) - 3):
            if(i>0 and nums[i] == nums[i-1]):
                i += 1
                continue
            if(nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target):
                break
            if(nums[i] +lastThreeSum < target):
                continue
            for j in range(i+1,len(nums)-2):
                if(nums[j] == nums[j-1] and j > i+1):
                    j += 1
                    continue
                if(nums[i]+nums[j]+nums[j+1]+nums[j+2] > target):
                    break
                if(nums[i]+nums[j] + lastTwoSum < target):
                    continue
                top = j + 1
                botten = len(nums) - 1
                while(top < botten):
                    fourSum = nums[i]+nums[j]+nums[top]+nums[botten]
                    if(fourSum < target):
                        top += 1
                        while nums[top] == nums[top-1] and top < botten:
                            top += 1
                    elif(fourSum > target):
                        botten -= 1
                        while nums[botten] == nums[botten+1] and top < botten:
                            botten -= 1
                    else:
                        result.append([nums[i],nums[j],nums[top],nums[botten]])
                        top += 1
                        while nums[top] == nums[top-1] and top < botten:
                            top += 1
                        botten -= 1
                        while nums[botten] == nums[botten+1] and top < botten:
                            botten -= 1
        return result
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''