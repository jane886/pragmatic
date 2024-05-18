"""
大顶堆（Max Heap）和小顶堆（Min Heap）是堆（Heap）数据结构的两种变体，它们在元素的排列顺序和堆属性上有所不同。
    大顶堆：
        在大顶堆中，父节点的值大于或等于其子节点的值。
        根节点是堆中的最大值。
        任意节点的值都大于或等于其子节点的值。
        大顶堆通常用于获取最大值或进行降序排列。
    小顶堆：
        在小顶堆中，父节点的值小于或等于其子节点的值。
        根节点是堆中的最小值。
        任意节点的值都小于或等于其子节点的值。
        小顶堆通常用于获取最小值或进行升序排列。

堆数据结构通常使用二叉树的形式来表示，其中父节点和子节点之间存在特定的关系。
在数组实现堆的情况下，可以使用下标关系来表示节点之间的关系。

大顶堆和小顶堆的操作（插入、删除等）基本相似，只是在维护堆属性时有所不同。
通过保持堆属性，可以高效地获取堆中的最大或最小值，并在插入或删除元素时进行自动调整。

需要注意的是，堆并不是排序算法，它是一种数据结构，用于满足最大或最小值的获取要求。
堆排序是一种基于堆数据结构的排序算法，它利用堆的特性对元素进行排序。

总结起来，大顶堆和小顶堆是堆数据结构的两种变体，它们的区别在于元素的排列顺序和堆属性。
大顶堆中父节点的值大于或等于子节点，小顶堆中父节点的值小于或等于子节点。
这两种堆可以用于获取最大或最小值，并在插入或删除元素时自动调整堆结构。
"""

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        
        self._swap(0, len(self.heap) - 1)
        max_val = self.heap.pop()
        self._sift_down(0)
        return max_val
    
    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        
        return self.heap[0]
    
    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2
    
    def _sift_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_index = index
            
            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] > self.heap[largest_index]):
                largest_index = left_child_index
            
            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] > self.heap[largest_index]):
                largest_index = right_child_index
            
            if largest_index == index:
                break
            
            self._swap(index, largest_index)
            index = largest_index
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        
        self._swap(0, len(self.heap) - 1)
        min_val = self.heap.pop()
        self._sift_down(0)
        return min_val
    
    def peek(self):
        if not self.heap:
            raise IndexError("Heap is empty")
        
        return self.heap[0]
    
    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2
    
    def _sift_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest_index = index
            
            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] < self.heap[smallest_index]):
                smallest_index = left_child_index
            
            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] < self.heap[smallest_index]):
                smallest_index = right_child_index
            
            if smallest_index == index:
                break
            
            self._swap(index, smallest_index)
            index = smallest_index
    
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


"""
在这个实现中，我们手动实现了大顶堆和小顶堆的数据结构。
MaxHeap 类代表大顶堆，MinHeap 类代表小顶堆。
它们都具有 push 插入元素、pop 弹出堆顶元素、peek 获取堆顶元素而不弹出的方法。
在内部，我们使用列表来存储堆的元素，并实现了 _sift_up 和 _sift_down 方法来维护堆的属性。
_sift_up 方法用于将插入的元素上移以满足堆属性，_sift_down 方法用于将根节点下移以满足堆属性。
_swap 方法用于交换两个元素的位置。
"""


def main():
    # 大顶堆示例
    max_heap = MaxHeap()
    max_heap.push(3)
    max_heap.push(2)
    max_heap.push(1)
    print(max_heap.peek())  # 输出：3
    print(max_heap.pop())   # 输出：3
    print(max_heap.peek())  # 输出：2

    # 小顶堆示例
    min_heap = MinHeap()
    min_heap.push(1)
    min_heap.push(2)
    min_heap.push(3)
    print(min_heap.peek())  # 输出：1
    print(min_heap.pop())   # 输出：1
    print(min_heap.peek())  # 输出：2