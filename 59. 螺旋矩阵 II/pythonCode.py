from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [n*[0] for _ in range(n)]
        c = 1
        i = 0
        while(c <= n*n):
            for j in range(i,n-i):
                matrix[i][j] = c
                c += 1
            for j in range(i+1,n-i):
                matrix[j][n-i-1] = c
                c+=1
            for j in range(n-i-2,i-1,-1):
                matrix[n-i-1][j] = c
                c+=1
            for j in range(n-i-2,i,-1):
                matrix[j][i] = c
                c+=1
            i+=1
        return matrix
'''

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''