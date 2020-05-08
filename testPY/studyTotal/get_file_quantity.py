#python 小技巧之获取固定目录下面包含的某种类型文件的个数
import glob
path_file_number=glob.glob(pathname='/Users/luoquan/PycharmProjects/b2b_api_oas_case_suite/testcase/test_oas_http/*/*.py')
print(path_file_number)
print(len(path_file_number))

