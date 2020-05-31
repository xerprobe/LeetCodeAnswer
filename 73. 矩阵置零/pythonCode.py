from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowFlag = False
        colFlag = False

        for i in range(len(matrix)):
            if(matrix[i][0] == 0):
                colFlag = True
                break
        for j in range(len(matrix[0])):
            if(matrix[0][j] == 0):
                rowFlag = True
                break
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if(matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,len(matrix)):
            if(matrix[i][0] == 0):
                matrix[i] = len(matrix[0])*[0]
        for j in range(1,len(matrix[0])):
            if(matrix[0][j] == 0):
                for i in range(1,len(matrix)):
                    matrix[i][j] = 0
        if(rowFlag):
            matrix[0] = len(matrix[0])*[0]
        if(colFlag):
            for i in range(len(matrix)):
                matrix[i][0] = 0
'''
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
示例 2:

输入: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
进阶:

一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
'''