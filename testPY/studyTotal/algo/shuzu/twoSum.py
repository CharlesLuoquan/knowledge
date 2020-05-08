'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
'''
class Solution:
    def twoSum(self, nums, target):
        #两个for循环，时间复杂度O(n2);没有定义存储空间，空间复杂度O(1)
        size=len(nums)
        for i in range(size-1):
            for j in range(i+1,size):
                if nums[i]+nums[j]== target:
                    # print(nums[i],nums[j])
                    return [i,j]
                else:
                    pass

    def twoSum_1(self, nums, target):
        #解法二：使用enumerate函数，时间O（n）空间O（n）
        dict={}
        for i,nums[i] in enumerate(nums):
            dict[nums[i]]=i

        for i,nums[i] in enumerate(nums):
            j=dict.get(target-nums[i])
            if j is not None and i != j:
                return [i,j]
    '''
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
    '''
    def twoSum_2(self, nums, target):
        dict = {}
        for i, nums[i] in enumerate(nums):
            dict[nums[i]] = i

        for i, nums[i] in enumerate(nums):
            j = dict.get(target - nums[i])
            if j is not None and i != j and i<j:
                return [i+1, j+1]






if __name__ == '__main__':
    # nums = [3,2,4]
    # nums = [2,5,5,11]
    nums =[2, 7, 11, 15]
    target=9
    a=Solution()
    print(a.twoSum_2(nums,target))