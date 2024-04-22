"""
在这个实现中，我们使用一个字典cache来存储键和对应的节点对象。每个节点对象包含键、值以及指向前一个节点和后一个节点的指针。
我们还维护了一个双向链表，通过在链表头部插入节点和从链表尾部弹出节点来表示最近使用和最久未使用的节点。
通过这种方式，我们可以实现LRU缓存的淘汰策略。


无论是使用OrderedDict还是自定义双向链表，上述实现都能保持put()和get()操作的时间复杂度为O(1)。

对于get()操作，通过使用字典（或OrderedDict）来存储缓存项，可以在常数时间内直接获取到相应的值。

对于put()操作，我们在字典中存储键和对应的节点对象，以及使用双向链表来维护节点的顺序。无论是在字典中插入键值对还是在链表中插入和删除节点，这些操作都可以在常数时间内完成。

因此，整体上，LRU缓存的put()和get()操作的平均时间复杂度为O(1)。
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)  # 头节点
        self.tail = Node(None, None)  # 尾节点
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        # 将节点插入到头节点之后
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # 从链表中移除节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        # 将节点移动到头部，表示最近使用
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # 弹出尾部节点，表示最久未使用
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)


# 示例用法
cache = LRUCache(2)
cache.put(1, "A")
cache.put(2, "B")
print(cache.get(1))  # 输出: "A"
cache.put(3, "C")  # 键2被淘汰
print(cache.get(2))  # 输出: -1，因为键2已被淘汰
cache.put(4, "D")  # 键1被淘汰
print(cache.get(1))  # 输出: -1，因为键1已被淘汰
print(cache.get(3))  # 输出: "C"
print(cache.get(4))  # 输出: "D"
