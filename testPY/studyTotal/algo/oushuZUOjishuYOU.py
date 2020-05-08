'''
一个list，里面的数字偶数在左边，奇数在右边，不借助其他列表
'''
def userlist(addlist):
    if type(addlist)==list :
        if len(addlist) == 1 and type(addlist[0]) == 'int':
            return addlist
        for item in addlist:
            try:
                if item%2 == 0:
                    addlist.remove(item)
                    addlist.insert(0, item)
            except :
                return "分母为0"
        return addlist
    else:
        return False
addlist=[1,3,4,5,6,7,8,9,2]
print(userlist(addlist))