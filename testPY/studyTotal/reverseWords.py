#import json

class Solution:
    def reverseWords(self, str):
        l=list(str)
        #reverse()内置函数，对l进行操作
        l.reverse()
        print(l)
        #通过join将其变回str
        re_str="".join(l)
        print(re_str)
    def reverseWordsTwo(self, str):
        #str.split()字符串分割成含子子字符串的列表(默认所有的空字符，包括空格、换行(\n)、制表符(\t)等);
        # [::-1]翻转字符串: 取从后向前（相反）的元素;
        # 再将其变成str通过空格区分
        s=" ".join(str.split()[::-1])
        print(s)


if __name__ == '__main__':
    a=Solution()
    #a.reverseWords('the sky is blue')
    a.reverseWordsTwo('the sky is blue')
    a.reverseWordsTwo('  hello world!  ')
    a.reverseWordsTwo('a good   example')