'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
'''
class Solution:
    def searchInsert0(self, nums, target):
        #数组，二分查找

        # if not nums:
        #     return 0
        # size=len(nums)
        # for i in range(size):
        #     if nums[i]==target:
        #         return i

        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i + j) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                i = m + 1
            else:
                j = m - 1
        return i



    def searchInsert1(self, nums, target):
        #list特性
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums=sorted(nums)
            return nums.index(target)
if __name__ == '__main__':
    a=Solution()
    print(a.searchInsert0([1,4,5,6,9,12],3))


