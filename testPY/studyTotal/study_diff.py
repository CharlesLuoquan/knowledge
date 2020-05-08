#coding=utf-8
import os

# pic='/Users/luoquan/Desktop/luopangpang/kobe.jpeg'
# pic_file = open(pic, 'rb')
# pic_file.close()
# files = {'picture': (os.path.basename(pic), pic_file, 'image/jpeg', {})}
# print(files)

def test_args(orderNo, *args):
    print('Required argument: ', orderNo)
    print(type(args))
    for v in args:
        print ('Optional argument: ', v)

# test_args(1, 2, 3, 4,"dadada",4,'dadad2222')

def test_kwargs(first, *args, **kwargs):
   print('Required argument: ', first)
   print(type(kwargs))
   for v in args:
      print ('Optional argument (args): ', v)
   for k, v in kwargs.items():
      print ('Optional argument %s (kwargs): %s' % (k, v))

test_kwargs({1:2},k1=5, k2=6)