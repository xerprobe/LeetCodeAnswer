class Solution:
    def countPrimes(self, n: int) -> int:
        nums = n * [1]
        ans = 0
        for i in range(2,n):
            if nums[i]:
                ans += 1
                x = i
                while(x < n):
                    nums[x] = 0
                    x += i
        return ans


# 统计所有小于非负整数 n 的质数的数量。

# 示例:

# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 链接：https://leetcode-cn.com/problems/count-primes/
