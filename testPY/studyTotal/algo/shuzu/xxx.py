def binary_search(l, target):
    length = len(l)
    R = length - 1
    L = 0

    while L <= R:
        mid = (L + R) // 2
        # 表示整数除法,返回不大于结果的一个最大的整数
        findx = l[mid]

        if findx == target:
            return mid
        if findx < target:
            # 中间数比待找值小
            L = mid + 1
        if findx > target:
            R = mid - 1

    return -1


al = [1, 2, 3, 4, 5, 6, 7, 8]
res = binary_search(al, 4)
print(res)
