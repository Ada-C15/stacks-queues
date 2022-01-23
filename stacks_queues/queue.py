
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
        if self.size == 0:
            self.front = 0

        elif self.size == self.buffer_size:
            raise QueueFullException("Error message")

        self.rear = (self.rear + 1) % self.buffer_size
        self.store[self.rear] = element
        self.size += 1
        return None

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        try:
            temp = self.store[self.front]
            self.store[self.front] = None
            self.front = (self.front + 1) % self.buffer_size
            self.size -= 1
            return temp
        except:
            raise QueueEmptyException("Error message")

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        try:
            return self.store[self.front]
        except:
            raise QueueEmptyException("Error message")

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        try:
            return self.size
        except:
            raise QueueEmptyException("Error message")
        

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        try:
            return self.size == 0
        except:
            raise QueueEmptyException("Error message")

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        nodes = []
        back = self.rear

        if self.size == 0:
            return nodes
        
        current = self.front

        while current != back:
            nodes.append(self.store[current])
            current = (current + 1) % self.buffer_size

        nodes.append(self.store[back])

        return str(nodes) 
