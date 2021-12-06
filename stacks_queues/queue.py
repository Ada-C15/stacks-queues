
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
        if self.size == self.buffer_size:
            raise QueueFullException('Queue is full')

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
            self.size += 1
            return self.store

        else:
            self.rear = (self.rear + 1) % self.buffer_size
            self.store[self.rear] = element
            self.size += 1
            return self.store


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.front == -1:
            raise QueueEmptyException('Queue is empty')

        else:
            element = self.store[self.front]
            self.front = (self.front + 1) % self.buffer_size
            self.size -= 1
            return element

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty(): 
            return None 
        
        else:
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
        if self.size == 0:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        
        queue_list = []

        if self.empty():
            return str(queue_list)

        for element in range(self.front, self.front + self.size):
            element = element % self.buffer_size
            queue_list.append(self.store[element])
        return str(queue_list)
