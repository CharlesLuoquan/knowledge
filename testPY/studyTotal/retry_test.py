import sys,os
import time,random

def run():
    re=random.random()
    print(re)
    if re > 0.3:
        raise Exception()

if __name__ == '__main__':
    a=run()
