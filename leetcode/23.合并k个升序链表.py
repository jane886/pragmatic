"""
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

示例 1：

输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
 

提示：

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        amount = len(lists)

        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2List(lists[i], list[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else None
    
    def merge2List(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = point = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                point.next = list1
                list1 = list1.next
            else:
                point.next = list2
                list2 = list1
                list1 = point.next.next
            point = point.next
        if not list1:
            point.next = list2
        else:
            point.next = list1
        return head.next


# 时间复杂度：O(Nlogk)，其中 k 是链表的数目
    # 我们可以在 O(n) 的时间内合并两个有序链表，其中 n 是两个链表的总节点数
    # 将所有合并过程加起来，我们可以得到 O(Nlogk)

# 时间复杂度：O(1)
    # 我们可以用 O(1) 的空间实现两个有序链表的合并