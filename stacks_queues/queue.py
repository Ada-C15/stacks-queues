INITIAL_QUEUE_SIZE = 20
class QueueFullException(Exception):
    pass
class QueueEmptyException(Exception):
    pass


class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = -1
        self.rear = -1
        self.size = 0
      
    def enqueue(self, element):
        if self.front == self.rear == -1:
            self.front = 0
            self.rear = 0
        
        self.capacity_max()
        
        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1

    def dequeue(self):
        if self.rear == self.front == -1:
            raise QueueEmptyException("Queue is empty")

        else:
            self.capacity_min()
            value = self.store[self.front]
            self.store[self.front] = None
            self.front = (self.front + 1) % self.buffer_size

        self.size -= 1
        return value

    def front(self):
        if self.front == -1:
            raise QueueEmptyException("Queue is empty")
        
        return self.store[self.front]
        
    def size(self):
        return self.size

    def resize_buffer(self, capacity):
        '''
            added resize to implementation for to resize circular buffer
        '''
        copy = [None] * capacity

        for i in range(0, self.size()):
            copy[i] = self[i + capacity]
        self = copy

    def capacity_max(self):
        '''
            helper method to adjust circular buffer to be big enough 
        '''
        if self.size == self.store:
            self.resize_buffer(self.size * 2)

    def capacity_min(self):
        '''
            helper method to ensure buffer isn't take more memory than really needed
        '''
        if self.size < (self.size / 4):
            self.resize_buffer(self.size / 2)

    def empty(self):
        return self.size == 0

    def __str__(self):
        values = []
        current = self.front
        count = 0

        while count < self.size:
            values.append(str(self.store[current]))
            current = (current + 1) % self.buffer_size
            count += 1

        return f"[{', '.join(values)}]"
