
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = []      

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if len(self.store) == INITIAL_QUEUE_SIZE:
            raise QueueFullException
        
        self.store.append(element)
    

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if len(self.store) == 0:
            raise QueueEmptyException
        
        return self.store.pop(0)


    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if len(self.store) == 0:
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
        return str(self.store)
