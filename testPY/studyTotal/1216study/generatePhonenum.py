#手机号注册,python实现随机生成手机号的代码
import random
def generate():
    list=['(联通)155','(联通)156','(联通)185']
    print(type(list))
    # 从序列中随机选取一个元素
    a=random.choice(list)
    print(a)
    shuzi='0123456789'
    str_shuzi=''
    num=[]
    for i in range(8):
        num.append(random.choice(shuzi))
        #序列中的元素以指定的字符连接生成一个新的字符串,用于将列表等转换为字符串
        str_shuzi=''.join(num)
    print(a+str_shuzi)


generate()