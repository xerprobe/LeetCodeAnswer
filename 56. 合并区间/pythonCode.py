from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.quick_sort(intervals,0,len(intervals) - 1)
        i = 0
        while(i < len(intervals) - 1):
            if(intervals[i][1] >= intervals[i+1][0]):
                left = intervals.pop(i)
                intervals[i] = [left[0],max(left[1],intervals[i][1])]
            else:
                i += 1
        return intervals

    def quick_sort(self, s: List[List[int]],l: int,r: int) -> None:
        if (l < r):
            i = l
            j = r
            x = s[l]
            while(i < j):
                while(i < j and s[j][0] >= x[0]):
                    j -= 1
                while(i < j and s[i][0] <= x[0]):
                    i += 1
                if(i < j):
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
            s[l] = s[i]
            s[i] = x
            self.quick_sort(s, l, i - 1) 
            self.quick_sort(s, i + 1, r)
'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''