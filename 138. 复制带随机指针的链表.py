"""
138. 复制带随机指针的链表
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

"""


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head: 'Node') -> 'Node':
    if not head:
        return None

    # 建立哈希表，用于存储原链表和新链表中每个节点的对应关系
    visited = {}

    # 创建新链表的头节点，并将原链表的头节点添加到哈希表中
    new_head = Node(head.val)
    visited[head] = new_head

    # 遍历原链表，同时创建新链表
    old_node = head
    new_node = new_head
    while old_node:
        # 复制 next 指针
        if old_node.next:
            if old_node.next not in visited:
                visited[old_node.next] = Node(old_node.next.val)
            new_node.next = visited[old_node.next]

        # 复制 random 指针
        if old_node.random:
            if old_node.random not in visited:
                visited[old_node.random] = Node(old_node.random.val)
            new_node.random = visited[old_node.random]

        # 指针后移
        old_node = old_node.next
        new_node = new_node.next

    return new_head

# 首先判断原链表是否为空，如果为空则返回空。然后创建哈希表和新链表的头节点，并将原链表的头节点添加到哈希表中。接着遍历原链表，同时创建新链表，并在遍历过程中处理随机指针的问题。最后返回新链表的头节点。

# 这个算法的时间复杂度是O(n)，其中n是原链表的长度。空间复杂度也是O(n)，因为需要使用哈希表来存储每个节点的对应关系。
