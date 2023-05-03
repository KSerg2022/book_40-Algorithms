import numpy as np

print('1 -- ')
myVector = [22, 33, 44, 55]
print(myVector)
print(type(myVector))

print('\n2 -- ')
myVector = np.array([22, 33, 44, 55])
print(myVector)
print(type(myVector))

print('\n3 -- ')
"""Stack"""


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push('1')
stack.push('10')
stack.push('100')
stack.push('1000')
print(stack)
print(stack.items)
print(stack.peek())
print(stack.size())

print('\n4 -- ')
"""Queue"""


class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(10)
queue.enqueue(100)
queue.enqueue(1000)
print(queue.items)
queue.dequeue()
print(queue.items)
queue.dequeue()
print(queue.items)

print('\n5 -- ')

print('\n6 -- ')
print('\n7 -- ')
print('\n8 -- ')
