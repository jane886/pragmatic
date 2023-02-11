"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零

"""
from typing import Optional

from utils import ensure


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 初始化 pre 为第一个节点，同时 head 指向第一个节点
        pre = ListNode(0)
        current = pre
        carry = 0
        # 分别遍历两个链表
        while l1 is not None or l2 is not None:
            # 开始相加 l1 和 l2 的值，用 sum 接住
            sum = 0
            if l1 is not None:
                sum += l1.val
                l1 = l1.next

            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            # 当 sum 值大于 10，carry 进 1 位，sum - 10
            sum += carry
            carry = sum // 10
            sum = sum % 10

            # 把 current 的下一位指向当前 sum 值的节点，然后把 current 指向 下一位
            current.next = ListNode(sum)
            current = current.next

        # 这里最后再加上 carry 的进位，假设最后两个数加起来超过 10 了
        if carry > 0:
            current.next = ListNode(carry)

        return pre.next







def node_list(l):
    head = ListNode(l[0])
    root = head
    for i in l[1:]:
        node = ListNode(i)
        root.next = node
        root = node
    return head


def node_to_list(result):
    l = []
    while result is not None:
        l.append(result.val)
        result = result.next
    return l


class Test:

    @classmethod
    def test1(cls):
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        node_list1 = node_list(l1)
        node_list2 = node_list(l2)
        s = Solution()
        r = node_to_list(s.addTwoNumbers(node_list1, node_list2))
        ensure(r, [7, 0, 8], "测试 1")

    @classmethod
    def test2(cls):
        l1 = [0]
        l2 = [0]
        node_list1 = node_list(l1)
        node_list2 = node_list(l2)
        s = Solution()
        r = node_to_list(s.addTwoNumbers(node_list1, node_list2))
        ensure(r, [0], "测试 2")

    @classmethod
    def test3(cls):
        l1 = [9, 9, 9, 9, 9, 9, 9]
        l2 = [9, 9, 9, 9]
        node_list1 = node_list(l1)
        node_list2 = node_list(l2)
        s = Solution()
        r = node_to_list(s.addTwoNumbers(node_list1, node_list2))
        ensure(r, [8, 9, 9, 9, 0, 0, 0, 1], "测试 3")


def main():
    t = Test()
    t.test1()
    t.test2()
    t.test3()


if __name__ == '__main__':
    main()
