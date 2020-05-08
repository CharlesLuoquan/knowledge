'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''
class Solution:
    def maxSubArray(self, nums):
        temp = max_ = nums[0]

        for i in range(1, len(nums)):

            if temp > 0:
                temp += nums[i]
            else:
                temp = nums[i]

            max_ = max(temp, max_)

        return max_


if __name__ == '__main__':
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    a=Solution()
    print(a.maxSubArray(nums))