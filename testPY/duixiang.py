def go_upstairs(num):
    if num == 1:
        return 1
    elif num ==2 :
        return 2
    elif num ==3:
        return 4
    else:
        return go_upstairs(num-1)+go_upstairs(num-2)+go_upstairs(num-3)
# num = input("请输入台阶数：")
# try:
#     num = int(num)
#     steps = go_upstairs(num)
#     print(steps)
# except Exception as e:
#     print("不是数字")

a = go_upstairs(5)
print(a)
