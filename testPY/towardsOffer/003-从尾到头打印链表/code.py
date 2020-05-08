'''
题目描述
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
思路
用栈存放，再输出:栈的数据结构是后进先出
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法1：用辅助栈存储
class Solution:
    def printListFromTailToHead(self, listNode):
        # # write code here
        # stack = []
        # result_array = []
        # node_p = listNode
        # while node_p:
        #     stack.append(node_p.val)
        #     node_p = node_p.next
        # while stack:
        #     result_array.append(stack.pop(-1))
        # return result_array
        if not listNode:
            return []
        temp = []
        result = []
        while listNode:
            temp.append(listNode.val)  # 进栈
            listNode = listNode.next
        while temp:
            result.append(temp.pop())  # 出栈
        return result


    # 解法2：本身栈调用
    # result_array = []
    # def printListFromTailToHead_1(listNode):
    #     # write code here
    #     if listNode:
    #         printListFromTailToHead(listNode.next)
    #         result_array.append(listNode.val)
    #     return result_array

class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []

        result = []
        head = listNode

        while head:
            result.insert(0, head.val)
            head = head.next
        return result

if __name__ == '__main__':
    a=Solution1()
    b=ListNode(x=[1,55,3,4,5])
    # print(b)
    re = a.printListFromTailToHead(b)
    print(re)


