from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1 = 0
        right1 = len(nums1) - 1
        left2 = 0
        right2 = len(nums2) - 1
        while(right1 >= left1 and right2 >= left2 ):
            if(right1 == left1 and right2 == left2):
                return (nums1[right1] + nums2[right2]) / 2
            if(nums1[left1] > nums2[left2]):
                left2 = left2 + 1
            else:
                left1 = left1 + 1
            if(nums1[right1] < nums2[right2]):
                right2 = right2 - 1
            else:
                right1 = right1 - 1
        if(right1 < left1):
            if((right2 - left2)%2):
                return (nums2[(right2+left2)//2] + nums2[(right2+left2)//2 + 1])/2
            else:
                return nums2[(right2+left2)//2]
        if(right2 < left2):
            if((right1 - left1)%2):
                return (nums1[(right1+left1)//2] + nums1[(right1+left1)//2 + 1])/2
            else:
                return nums1[(right1+left1)//2]
'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

 

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''