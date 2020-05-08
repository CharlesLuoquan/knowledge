class Solution:
    def lengthOfLongestSubstring(self, s):
        l = 0
        start = 0
        dic = {}
        for i in range(len(s)):
            cur = s[i]
            if cur not in dic.keys():
                dic[cur] = i
            else:
                if dic[cur] + 1 > start:
                    start = dic[cur] + 1
                    dic[cur] = i
            if i - start + 1 > l:
                    l = i - start + 1
        return l


if __name__ == '__main__':
    a=Solution()
    re=a.lengthOfLongestSubstring('abcabcbb')
    print(re)