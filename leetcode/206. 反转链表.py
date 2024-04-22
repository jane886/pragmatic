"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

"""
from typing import List, Optional

from utils import ensure

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = pre
            pre = curr
            curr = next_node
        return pre
        
# 复杂度分析

    # 时间复杂度：O(n)，其中 n 是链表的长度。需要遍历链表一次。

    # 空间复杂度：O(1)。