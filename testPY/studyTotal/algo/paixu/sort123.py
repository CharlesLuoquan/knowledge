class Solution:
    def bubble_sorted(self, nums):
        #冒泡排序
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]

        return nums
    def insert_sort(self, nums):
        #插入排序
        size=len(nums)
        if size==1:
            return nums
        for i in range(1, size):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                else:
                    break
        return nums

if __name__ == '__main__':
    a=Solution()
    nums=[27, 33, 28, 4, 2, 26, 13, 35, 8, 14]
    # nums=[3]
    # print(a.bubble_sorted(nums))
    print(a.insert_sort(nums))