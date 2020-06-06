from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums: return 0
        def binarySearch(l:int,r:int) -> int:
            if(nums[l] < nums[r]):
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                return binarySearch(mid,r)
            elif nums[mid] < nums[r]:
                return binarySearch(l,mid)
            else:
                return nums[r]
        return binarySearch(0,len(nums) - 1)

# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 你可以假设数组中不存在重复元素。

# 示例 1:

# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:

# 输入: [4,5,6,7,0,1,2]
# 输出: 0

# 链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array