
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

        if (self.rear + 1) % self.buffer_size == self.front:
            raise QueueFullException()
        
        elif self.empty():
            self.front = 0
            self.rear = 0

        self.store[self.rear] = element
        self.rear = (self.rear + 1) % self.buffer_size
        self.size +=1

        return None

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty(): 
            raise QueueEmptyException()
        
        element = self.store[self.front]
        self.front = (self.front+1)%self.buffer_size
        self.size-=1 

        return element


    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.isEmpty():
            return -1
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
        arr = []

        for i in range(self.front, self.rear, 1):
            if self.store[i]:
                arr.append(self.store[i])

        return str(arr)
        
