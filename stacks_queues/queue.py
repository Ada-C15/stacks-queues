
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
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.front == self.rear == -1:
            self.front = 0
            self.rear = 0
        elif self.rear == self.front:
            raise QueueFullException(f"Queue is full, cannot add {element}")
        
        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
        """
        if self.rear == self.front == -1:
            raise QueueEmptyException("Queue is empty")
        else:
            value = self.store[self.front]
            self.store[self.front] = None
            self.front = (self.front + 1) % self.buffer_size
            if self.front == self.rear:
                self.rear = self.front = -1
        
        self.size -= 1
        return value

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.front == -1:
            raise QueueEmptyException("Queue is empty")
        
        return self.store[self.front]
        
    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        values = []
        current = self.front
        count = 0

        while count < self.size:
            values.append(str(self.store[current]))
            current = (current + 1) % self.buffer_size
            count += 1

        return f"[{', '.join(values)}]"
