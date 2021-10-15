
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
            raise QueueFullException()
        if self.size == 0:
            self.front = 0
        self.rear = (self.rear + 1) % self.buffer_size
        self.size += 1
        self.store[self.rear] = element

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException()
        # front_value = self.store[self.front]

        front_value = self.front_value() 
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1
        return front_value
    #Want to use self.front() to get the front value, but self.front is already an attribute name
    #change it to front_value
    def front_value(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None
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
        for i in range(self.front, self.front + self.size):
            i = i % self.buffer_size
            values.append(self.store[i])
        return str(values)
