
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
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.front:
            raise QueueFullException(f"Queue is full, cannot add {element}")
        
        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1

    def dequeue(self):
        if self.rear == -1 and self.front == -1:
            raise QueueEmptyException("Queue is empty")
        else:
            returned_value = self.store[self.front]
            self.store[self.front] = None
            self.front = (self.front + 1) % self.buffer_size
            if self.front == self.rear:
                self.rear = self.front = -1
        
        self.size -= 1
        return returned_value

    def front(self):
        if self.front == -1:
            raise QueueEmptyException("Queue is empty")
        
        return self.store[self.front]
        

    def size(self):
        return self.size

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
