from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            other = target - num
            if(self.bans(numbers,other)):
                otherIndex = numbers.index(other)
                if(otherIndex == index):
                    if(numbers[otherIndex + 1] == numbers[otherIndex]):
                        return [index+1, index+2]
                    else:
                        continue
                else:
                    return [index + 1, otherIndex+1]
        return [0, 0]
    def bans(self,numbers: List[int],target: int) -> bool:
        if(target < numbers[0] or target > numbers[-1]):
            return False
        else:
            if(target > numbers[len(numbers)//2]):
                return self.bans(numbers[len(numbers)//2+1:len(numbers)],target)
            elif(target < numbers[len(numbers)//2]):
                return self.bans(numbers[0:len(numbers)//2],target)
            else:
                return True
'''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''