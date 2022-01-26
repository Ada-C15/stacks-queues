
from logging import raiseExceptions


INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

# queue = Queue()

# queue.enqueue(1)
# print(str(queue)) # [Object Queue]

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
        if self.get_size() + 1 > INITIAL_QUEUE_SIZE:
            raise QueueFullException("Queue is full")
        
        queue = self.store
        if queue != None:
            queue.append(element)
    

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        result = self.store.pop(0)
        if result is None:
            return self.dequeue()
        return result

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        pass
        

    def get_size(self):
        """ Returns the number of elements in
            The Queue
        """
        list_where_not_none = [x for x in self.store if x is not None]
        return len(list_where_not_none)

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        pass

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return self.get_size() == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        return str([x for x in self.store if x is not None])

