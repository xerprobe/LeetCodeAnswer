from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = r//2
        while(l <= r):
            if(nums[l] > nums[mid]): # 右侧有序
                if(nums[mid] <= target and nums[r] >= target):
                    return self.binarySearch(nums,mid,r,target)
                else:
                    r = mid
                    mid = (l + r) // 2
            elif(nums[l] < nums[mid]): # 左侧有序
                if(nums[mid] >= target and nums[l] <= target):
                    return self.binarySearch(nums,l,mid,target)
                else:
                    l = mid
                    mid = (l + r) // 2
            else:
                if(nums[l] == target):
                    return l
                elif(nums[r] == target):
                    return r
                break
        return -1

    def binarySearch(self, nums: List[int], l: int, r: int, target: int) -> int:
        mid = (l + r) // 2
        if(r - l <= 1):
            if(nums[l] == target): return l
            elif(nums[r] == target): return r
            else: return -1
        if(nums[mid] == target):
            return mid
        elif(target > nums[mid]):
            return self.binarySearch(nums,mid,r,target)
        elif(target < nums[mid]):
            return self.binarySearch(nums,l,mid,target)

'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''