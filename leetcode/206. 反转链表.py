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
        


def main():
    pass


if __name__ == '__main__':
    main()
