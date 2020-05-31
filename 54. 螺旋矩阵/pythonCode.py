from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        down = len(matrix) -1
        if(down < 0): return matrix
        right = len(matrix[0]) -1
        result = []
        up = 0
        left = 0
        while(up <= down and left <= right):
            for i in range(left,right+1):
                result.append(matrix[up][i])
            up += 1
            if(up > down):
                break
            for i in range(up,down+1):
                result.append(matrix[i][right])
            right -= 1
            if(left > right):
                break
            for i in range(right,left-1,-1):
                result.append(matrix[down][i])
            down -= 1
            if(up > down):
                break
            for i in range(down,up-1,-1):
                result.append(matrix[i][left])
            left += 1
        return result
'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
'''