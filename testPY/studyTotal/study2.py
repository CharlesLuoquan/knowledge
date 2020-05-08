class Solution:
    def twoSum(self, nums, target):
        l=len(nums)
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    return [i,j]
    def twoSum_plan2(self, nums, target):
        if not nums:
            return None

        d = dict()
        for i, item in enumerate(nums):
            tmp = target - item
            if tmp in d:
                return [i, d[tmp]]
            d[item] = i

        return None





if __name__ == '__main__':
    a=Solution()
    nums=[2, 7, 11, 15]
    target=9
    re=a.twoSum_plan2(nums,target)
    print(re)

