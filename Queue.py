class Queue:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        else:
            self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.items[0]


q = Queue(3)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.is_full())    # True
print(q.peek())       # 10
print(q.dequeue())    # 10
print(q.dequeue())    # 20
print(q.is_empty())   # False
