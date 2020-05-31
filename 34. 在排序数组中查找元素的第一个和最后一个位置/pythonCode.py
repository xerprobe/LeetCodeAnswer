from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        l = self.binarySearchLeft(nums,target)
        r = self.binarySearchRight(nums,target)
        return [l,r]


    def binarySearchLeft(self, nums: List[int],target: int) -> int:
        low = 0
        high = len(nums) - 1
        while(low < high):
            mid = (low + high) >> 1
            if(nums[mid] >= target):
                high = mid
            else:
                low = mid + 1
        return low if(nums[low] == target) else -1

    def binarySearchRight(self,nums: List[int], target: int):
        low = 0
        high = len(nums) - 1
        while(low < high):
            mid = ((low + high) >> 1) + 1
            if(nums[mid] <= target):
                low = mid
            else:
                high = mid - 1
        return high if(nums[high] == target) else -1
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''