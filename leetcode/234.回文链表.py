"""
给你一个单链表的头节点 head ，请你判断该链表是否为
回文链表
。如果是，返回 true ；否则，返回 false 。

 

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false
 

提示：

链表中节点数目在范围[1, 105] 内
0 <= Node.val <= 9
 

进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]
# 复杂度分析
    # 时间复杂度：O(n)，其中 nnn 指的是链表的元素个数。
    # 第一步： 遍历链表并将值复制到数组中，O(n)。
    # 第二步：双指针判断是否为回文，执行了 O(n/2) 次的判断，即 O(n)。
    # 总的时间复杂度：O(2n)=O(n)。
    
    #  空间复杂度：O(n)，其中 n 指的是链表的元素个数，我们使用了一个数组列表存放链表的元素值。


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        # 通过快慢指针，慢指针一次走一步，快指针一次走两步
        # 快指针的速度是慢指针的二倍。
        # 快指针速度2V，慢指针的速度就是V，两个指针同时开始走，快指针用时间T到达终点，慢指针用的时间也是T。
        # 这时快指针走过的路程S=2VT，慢指针走过的是路程S=VT。快指针走过的S=2VT表示的是全程，
        # 因此慢指针走过的刚好是一半（也就是中点）。
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
# 复杂度分析
    # 时间复杂度：O(n)，其中 nnn 指的是链表的大小。
    # 空间复杂度：O(1)。我们只会修改原本链表中节点的指向，而在堆栈上的堆栈帧不超过 O(1)