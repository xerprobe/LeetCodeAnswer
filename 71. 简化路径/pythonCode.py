class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cache = ''
        index = 0
        result = ''
        for i in path:
            if(i == '/' and cache.find(i) != -1):
                stack.append(cache)
                cache = i
            else:
                cache = cache + i
        stack.append(cache)
        while(index < len(stack)):
            if(len(stack[index]) == 1):
                stack.pop(index)
                continue
            else:
                if(stack[index] == '/..'):
                    if(index > 0):
                        stack.pop(index)
                        index -= 1
                        stack.pop(index)
                    else:
                        stack.pop(index)
                elif(stack[index] == '/.'):
                    stack.pop(index)
                else:
                    index += 1
        for i in stack:
            result = result + i
        return result if len(result) else '/'
'''
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

 

示例 1：

输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
示例 4：

输入："/a/./b/../../c/"
输出："/c"
示例 5：

输入："/a/../../b/../c//.//"
输出："/c"
示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"
'''