
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = []
        self.buffer_size = INITIAL_QUEUE_SIZE

        

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.empty() or len(self.store) < self.buffer_size:
            self.store.append(element)
        else: 
            raise QueueFullException("Queue is full")
        
    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
        """
        if self.empty():
            raise QueueEmptyException("Queue is empty")
        else:
            return self.store.pop(0)

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None
        else:
            return self.store[0]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return len(self.store)
        

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return len(self.store) == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.empty():
            return self.store
        else:
            return f'{self.store}'

        
