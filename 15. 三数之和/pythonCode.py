from typing import List

class Solution:
    def threeSum(self, numbers: List[int]) -> List[List[int]]:
        result = []
        numbers = sorted(numbers)
        if(len(numbers) < 3):
            return result
        if(numbers[-1] < 0 or numbers[0] > 0):
            return result
        if(0 in numbers):
            if(numbers[0] == 0):
                if(numbers[1] == 0 and numbers[2] == 0):
                    result.append([0,0,0])
                return result
            if(numbers[-1] == 0):
                if(numbers[-2] == 0 and numbers[-3] == 0):
                    result.append([0,0,0])
                return result
            if(len(numbers) - numbers.index(0) > 2 and numbers[numbers.index(0) + 1] == 0 and numbers[numbers.index(0) + 2] == 0):
                result.append([0,0,0])
        for num in set(numbers):
            frontList = []
            lastList = []
            if(num > 0):
                lastIndex, _ = self.getZeroIndex(numbers)
                frontIndex = 0
            elif(num < 0):
                _, frontIndex = self.getZeroIndex(numbers)
                lastIndex = len(numbers) - 1
            else:
                frontIndex = 0
                lastIndex = len(numbers) - 1
            while frontIndex != lastIndex :
                frontNum = numbers[frontIndex]
                lastNum = numbers[lastIndex]
                sumFL = frontNum + lastNum
                if(sumFL > -num):
                    lastIndex = lastIndex - 1
                    continue
                elif(sumFL < -num):
                    frontIndex = frontIndex + 1
                    continue
                else:
                    if(frontNum == 0 and lastNum == 0):
                        frontIndex = frontIndex + 1
                        continue
                    if(frontNum in frontList and lastNum in lastList):
                        frontIndex = frontIndex + 1
                        continue
                    element = [num,frontNum,lastNum]
                    element = sorted(element)
                    frontList.append(frontNum)
                    lastList.append(lastNum)
                    result.append(element)
                    frontIndex = frontIndex + 1
        return result
    
    def getZeroIndex(self,numbers: List[int]):
        if(0 in numbers):
            firstIndex = numbers.index(0)
            lastIndex = len(numbers) - 1 - numbers[::-1].index(0)
            return firstIndex - 1,lastIndex + 1
        firstIndex = 0
        while(numbers[firstIndex+1]<0):
            firstIndex = firstIndex + 1
        return firstIndex,firstIndex+1
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''