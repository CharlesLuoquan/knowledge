import requests
import urllib3
import logging
import re

#不发生告警
#urllib3.disable_warnings()

logging.captureWarnings(True)
r1=requests.get("https://www.douban.com/", verify=False)
# print(r1.status_code)
# print(r1.cookies)
# print(r1.url)
# print(r1.text)
#pattern = re.compile('\d+')   # 查找数字
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)

print(pattern)