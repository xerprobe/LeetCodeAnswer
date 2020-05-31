class Solution:
    def nthUglyNumber(self, num: int) -> int:
        if(num < 1):
            return
        else:
            num = num - 1
        a = [1]
        index2 = 0
        index3 = 0
        index5 = 0
        for _ in range(num):
            tmp = min(a[index2]*2,a[index3]*3,a[index5]*5)
            a.append(tmp)
            if(a[index2]*2 == tmp):
                index2 = index2 + 1
            if(a[index3]*3 == tmp):
                index3 = index3 + 1
            if(a[index5]*5 == tmp):
                index5 = index5 + 1
        return a[-1]

'''
编写一个程序，找出第 n 个丑数。

丑数就是质因数只包含 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。
'''