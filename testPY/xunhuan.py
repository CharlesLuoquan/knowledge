# nums = [5, 2, 5, 2, 2]
# for x in range(1, len(nums)+1):
# #     print(nums[x-1]*'x')
# for i in nums:
#     output = ''
#     for count in range(i):
#         output += 'x'
#     print(output)
def find_max(nums):
    # nums = [3, 6, 2, 8, 4]
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max


