# a=input()
#
# b=input()
#
# print('a+b={}'.format(a+b))
#
# print('type a is {},type b is {}'.format(type(a),type(b)))
#
# print('a+b={}'.format(int(a)+int(b)))
# def aa1(name='luo',age=20):
#     print(name)
#     print(age)
# aa1()

# print(type(info))
def aa2(**info):
    for i in info:
        print(info[i])


aa2(a=1,b=3,count=44)

def aa3(*orderNO):
    print(orderNO)
    print(type(orderNO))
    l=[]
    for i in orderNO:
        l.append(i)
    print(l)



info='kl111'
info2='kl001'
aa3(info,info2,'kl003')
