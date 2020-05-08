'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

'''
class Solution:
    def removeDuplicates(self, nums):
        #想不到
        i = 0
        for num in nums:
            if nums[i] != num:
                i += 1
                nums[i] = num
        return len(nums) and i+1


    def removeDuplicates_good(self, nums):
        #双指针，O（n）
        # 如果数组为空, 则返回0
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k


    def removeDuplicates_good_1(self, nums):
        #O（n2）,删除的时间复杂度是O（n）
        pre, cur = 0, 1
        while cur < len(nums):
            if nums[pre] == nums[cur]:
                nums.pop(cur)
            else:
                pre, cur = pre + 1, cur + 1
        return len(nums)


    def removeElement(self, nums, val):
        if not nums:
            return 0
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

    def removeElement_2(self, nums, val):
        while (val in nums):
            nums.remove(val)
        return len(nums)








if __name__ == '__main__':
    a=Solution()
    nums=[1,1,2,3,3,4]
    re=a.removeDuplicates_good(nums)
    print(re)
    print(nums)