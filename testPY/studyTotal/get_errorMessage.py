import os
import re



# with open('/Users/luoquan/PycharmProjects/b2b_api_case_core/utility/logging_report/logs/2019-06-20.log', 'r') as f:
#     print(f.read())

file_list=[]
for filename in os.listdir('/Users/luoquan/PycharmProjects/b2b_api_case_core/utility/logging_report/logs'):
    file_list.append(filename)
#print(file_list)
print(file_list[-1])
print(type(file_list[-1]))

# with open('/Users/luoquan/PycharmProjects/b2b_api_case_core/utility/logging_report/logs/2019-06-20.log', 'r') as f:
# fp = open("/Users/luoquan/PycharmProjects/testPY/study1.py", mode='r')
# fp.close()
fp=open('/Users/luoquan/PycharmProjects/b2b_api_case_core/utility/logging_report/logs/%s' %file_list[-1],'r',encoding="utf8")
content=fp.read()
fp.close()
#print(content)



pattern=re.compile('Finish executing testcase')
re1=pattern.findall(content)
print(re1)
