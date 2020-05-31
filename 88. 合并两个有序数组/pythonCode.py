from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = n-1
        s = m + n - 1
        while(i>=0 and j>=0):
            if(nums1[i] > nums2[j]):
                nums1[s] = nums1[i]
                i -= 1
            else:
                nums1[s] = nums2[j]
                j -= 1
            s -= 1
        nums1[:j+1] = nums2[:j+1]
'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''