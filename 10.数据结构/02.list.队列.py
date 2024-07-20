# list 实现队列

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]     # 队首元素

    def __str__(self):
        return str(self.items)

queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print("队首元素:", queue.peek())    # 输出: 队首元素: a
print("队列大小:", queue.size())    # 输出: 队列大小: 3

print("移除的元素:", queue.dequeue())  # 输出: 移除的元素: a
print("队列是否为空:", queue.is_empty())  # 输出: 队列是否为空: False
print("队列大小:", queue.size())    # 输出: 队列大小: 2