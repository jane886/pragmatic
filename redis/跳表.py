"""
1，跳表和有序链表的区别是什么？
答：跳表是有序链表的升级版，跳表的查询效率更高，但是跳表的插入和删除效率更低。


"""

# 实现跳表
import random


class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.next = [None] * level


class SkipList:
    def __init__(self, max_level=16):
        self.max_level = max_level
        self.level = 1
        self.head = SkipListNode(None, self.max_level)
        print("head.next", self.head.next)
        self.tail = SkipListNode(None, self.max_level)

        for i in range(self.max_level):
            self.head.next[i] = self.tail

    def find(self, value):
        p = self.head
        for i in range(self.level - 1, -1, -1):
            while p.next[i].value is not None and p.next[i].value < value:
                p = p.next[i]
        p = p.next[0]
        if p.value == value:
            return p
        else:
            return None

    def insert(self, value):
        level = self.random_level()
        if level > self.level:
            for i in range(self.level, level):
                self.head.next[i] = self.tail
            self.level = level

        p = self.head
        update = [None] * level
        for i in range(level - 1, -1, -1):
            while p.next[i].value is not None and p.next[i].value < value:
                p = p.next[i]
            update[i] = p

        node = SkipListNode(value, level)
        for i in range(level):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node

    def delete(self, value):
        p = self.head
        update = [None] * self.level
        for i in range(self.level - 1, -1, -1):
            while p.next[i].value is not None and p.next[i].value < value:
                p = p.next[i]
            update[i] = p

        if p.next[0].value == value:
            for i in range(self.level):
                if update[i].next[i] != p.next[i]:
                    break
                update[i].next[i] = p.next[i].next[i]

            while self.level > 1 and self.head.next[self.level - 1] == self.tail:
                self.level -= 1

    def random_level(self, p=0.25):
        level = 1
        while random.random() < p and level < self.max_level:
            level += 1
        return level

    def print_all(self, node=None):
        if node is None:
            node = self.head
        while node is not None:
            print(node.value, end=' ')
            node = node.next[0]
        print()


s = SkipList()
print(s)