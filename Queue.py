""" A simple implementation of a queue data structure. """


class Queue:
    """ Represents a queue using a Python list. """

    def __init__(self, size):
        """ Initializes the queue with a maximum size. """
        self.items = []
        self.size = size

    def is_empty(self):
        """ Checks if the queue is empty. """
        return len(self.items) == 0

    def is_full(self):
        """ Checks if the queue is full. """
        return len(self.items) == self.size

    def enqueue(self, item):
        """ Adds an item to the queue. """
        if self.is_full():
            print("Queue is full")
        else:
            self.items.append(item)

    def dequeue(self):
        """ Removes and returns the first item from the queue. """
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.items.pop(0)

    def peek(self):
        """ Returns the first item in the queue without removing it. """
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
