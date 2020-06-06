from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def infect(i: int, j: int) -> None:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            infect(i-1,j)
            infect(i+1,j)
            infect(i,j-1)
            infect(i,j+1)
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == '1'):
                    num += 1
                    infect(i,j)
        return num

# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

#  

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

# 链接：https://leetcode-cn.com/problems/number-of-islands