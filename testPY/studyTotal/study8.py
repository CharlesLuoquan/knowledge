class Solution:
    def reOrderArray(self, array):
        # write code here
        J = []
        O = []
        L = []
        for i in range(len(array)):
            if array[i]%2 == 0:
                J.append(array[i])
            else:
                O.append(array[i])
        return sorted(O)+sorted(J)

if __name__ == '__main__':
    a=Solution()
    b=a.reOrderArray([2,3,1,4,5,6,3,12,3])
    print(b)