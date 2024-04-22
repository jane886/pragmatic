"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。


示例 1：
输入：list1 = [1,2,4], list2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：list1 = [], list2 = []
输出：[]
示例 3：

输入：list1 = [], list2 = [0]
输出：[0]


提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
list1 和 list2 均按 非递减顺序 排列

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)

        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next            
            prev = prev.next

        # 合并后 list1 和 list2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = list1 if list1 is not None else list2

        return prehead.next


# 复杂度分析
    # 时间复杂度：O(n+m)，其中 n 和 m 分别为两个链表的长度。
    # 因为每次循环迭代中，list1 和 list2 只有一个元素会被放进合并链表中， 
    # 因此 while 循环的次数不会超过两个链表的长度之和。所有其他操作的时间复杂度都是常数级别的，因此总的时间复杂度为 O(n+m)。
    
    # 空间复杂度：O(1)。我们只需要常数的空间存放若干变量。
