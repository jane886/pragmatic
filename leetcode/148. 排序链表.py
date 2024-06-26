"""
148. 排序链表
中等

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
 

进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
「147. 对链表进行插入排序」要求使用插入排序的方法对链表进行排序，插入排序的时间复杂度是 O(n2)，其中 n 是链表的长度。
这道题考虑时间复杂度更低的排序算法。题目的进阶问题要求达到 O(nlog⁡n) 的时间复杂度和 O(1) 的空间复杂度，
时间复杂度是 O(nlog⁡n) 的排序算法包括归并排序、堆排序和快速排序（快速排序的最差时间复杂度是 O(n2)），其中最适合链表的排序算法是归并排序。

归并排序基于分治算法。最容易想到的实现方式是自顶向下的递归实现，考虑到递归调用的栈空间，
自顶向下归并排序的空间复杂度是 O(log⁡n)。如果要达到 O(1) 的空间复杂度，则需要使用自底向上的实现方式。

方法一：自顶向下归并排序

    对链表自顶向下归并排序的过程如下。

    找到链表的中点，以中点为分界，将链表拆分成两个子链表。
    寻找链表的中点可以使用快慢指针的做法，快指针每次移动 2 步，慢指针每次移动 1 步，
    当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。

    对两个子链表分别排序。

    将两个排序后的子链表合并，得到完整的排序后的链表。
    可以使用「21. 合并两个有序链表」的做法，将两个有序的子链表进行合并。

    上述过程可以通过递归实现。递归的终止条件是链表的节点个数小于或等于 1，
    即当链表为空或者链表只包含 1 个节点时，不需要对链表进行拆分和排序。
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))
            
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        return sortFunc(head, None)


# 复杂度分析
    # 时间复杂度：O(nlog⁡n)，其中 nnn 是链表的长度。
    # 空间复杂度：O(log⁡n)，其中 nnn 是链表的长度。空间复杂度主要取决于递归调用的栈空间。

"""
方法二：自底向上归并排序

    使用自底向上的方法实现归并排序，则可以达到 O(1) 的空间复杂度。

    首先求得链表的长度 length，然后将链表拆分成子链表进行合并。

    具体做法如下。

    用 subLength 表示每次需要排序的子链表的长度，初始时 subLength=1。

    每次将链表拆分成若干个长度为 subLength 的子链表（最后一个子链表的长度可以小于 subLength，
    按照每两个子链表一组进行合并，合并后即可得到若干个长度为 subLength×2 的有序子链表（最后一个子链表的长度可以小于 subLength×2。
    合并两个子链表仍然使用「21. 合并两个有序链表」的做法。

    将 subLength 的值加倍，重复第 2 步，对更长的有序子链表进行合并操作，直到有序子链表的长度大于或等于 length，整个链表排序完毕。

    如何保证每次合并之后得到的子链表都是有序的呢？可以通过数学归纳法证明。

    初始时 subLength=1，每个长度为 1的子链表都是有序的。

    如果每个长度为 subLength 的子链表已经有序，合并两个长度为 subLength 的有序子链表，得到长度为 subLength×2 的子链表，一定也是有序的。

    当最后一个子链表的长度小于 subLength 时，该子链表也是有序的，合并两个有序子链表之后得到的子链表一定也是有序的。

    因此可以保证最后得到的链表是有序的。
"""
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next
        
        if not head:
            return head
        
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break
                
                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                
                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1
        
        return dummyHead.next


# 复杂度分析
    # 时间复杂度：O(nlog⁡n)，其中 n 是链表的长度。
    # 空间复杂度：O(1)。
