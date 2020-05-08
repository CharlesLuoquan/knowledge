# l = [1, 2, 3, 4, 5, 6, 7]
# for index in range(0, len(l)):
#     if index < 5:
#         print(l[index])
#
# l = [1, 2, 3, 4, 5, 6, 7]
# for index,item in enumerate(l):
#     if index<5:
#         print(index,item)

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], ['mike', '1999-01-01', 'male'],['nancy', '2001-02-01', 'female']]


l=[]
for i in values:
    #print(i)
    #print(dict(zip(attributes,i)))
    #print(l.append(dict(zip(attributes,i))))
    l.append(dict(zip(attributes, i)))
print(l)

l=[]

for value in values:
    d={}
    for a in range(3):
        d[attributes[a]]=value[a]
    l.append(d)
print(l)

class Solution:
    def lengthOfLongestSubstring(self, str):

        print(str)
if __name__ == '__main__':

    re=Solution()
    re.lengthOfLongestSubstring(str='dddd')

