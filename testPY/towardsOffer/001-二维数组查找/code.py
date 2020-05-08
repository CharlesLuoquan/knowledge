'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
分治解题思路:
从右上角(或者左下角)开始查找：
如果target更大，指针下移
如果target更小，指针左移
'''
class Solution:
    def find(self, target, array):
        if len(array) == 0:
            return False
        i = 0
        j = len(array[0])-1
        while i < len(array) and j>=0:
            base = array[i][j]
            if target == base:
                return True
            elif target > base:
                i += 1
            else:
                j -= 1
        return False



if __name__ == '__main__':
    a=Solution()
    array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    array1 = []
    re = a.find(4, array1)
    print(re)