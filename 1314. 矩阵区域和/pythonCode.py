from typing import List
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if K >= m and K >= n:
            matSum = sum([sum(mat[i]) for i in range(m)])
            return [n*[matSum] for _ in range(m)]
        else:
            P = [[0] * (n+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + mat[i-1][j-1]
            answer = [[0]* n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    answer[i][j] = P[min(i + K + 1,m)][min(j + K + 1,n)] + P[max(i-K,0)][max(j-K,0)] - P[max(i-K,0)][min(j + K + 1,n)] - P[min(i + K + 1,m)][max(j - K,0)]
            return answer


# 给你一个 m * n 的矩阵 mat 和一个整数 K ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

# i - K <= r <= i + K, j - K <= c <= j + K 
# (r, c) 在矩阵内。
 

# 示例 1：

# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
# 示例 2：

# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
 

# 提示：

# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100
# 链接：https://leetcode-cn.com/problems/matrix-block-sum/
