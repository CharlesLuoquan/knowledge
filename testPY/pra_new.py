# b_map = {
#             '>' : '<',
#             ')' : '(',
#             '}' : '{',
#             ']' : '['
# }
# l_b = b_map.values()
# r_b = b_map.keys()
#
# def check(s):
#     b_list = list()
#     for b in s:
#         if b in l_b:
#             b_list.append(b)
#         if b in r_b:
#             if b_list and b_map[b] == b_list[-1]:
#                 b_list.pop()
#             else:
#                 return "no"
#     return "no" if b_list else "yes"
#
# if __name__ == '__main__':
#     while True:
#         s = input("输入测试数据:\n ")
#         if len(s) > 1000:
#             print("测试数据过长！")
#             continue
#         print(check(s))
a='abc'
print(a*2)
import datetime,time
print(datetime.datetime.today())
date_today = str(datetime.datetime.today()).split(' ')[0]
print(date_today)