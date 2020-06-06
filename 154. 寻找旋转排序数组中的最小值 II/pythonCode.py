from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        def binarySearch(l:int,r:int) -> int:
            if(nums[l] < nums[r] or l == r):
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                return binarySearch(mid,r)
            elif nums[mid] < nums[r]:
                return binarySearch(l,mid)
            else:
                if(nums[l] == nums[r]):
                    return min(binarySearch(mid+1,r),binarySearch(l,mid))
                elif(nums[l] == nums[mid]):
                    return binarySearch(mid+1,r)
                else:
                    return binarySearch(l,mid)
        return binarySearch(0,len(nums) - 1)

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 注意数组中可能存在重复的元素。

# 示例 1：

# 输入: [1,3,5]
# 输出: 1
# 示例 2：

# 输入: [2,2,2,0,1]
# 输出: 0
# 说明：

# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

# 链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii