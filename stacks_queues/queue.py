
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
        # if self.buffer_size > 20:
        #     raise QueueFullException()
        is_added = False
        for i in range(len(self.store)):
            if self.store[i] is None:
                self.store[i] = element
                is_added = True
                break
        if not is_added:
            raise QueueFullException
        

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException
        val = self.store[0]
        self.store.pop(0)
        self.store.append(None)
        return val
        
        


    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        return self.store[0]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        count = 0
        for element in self.store:
            if element is not None:
                count += 1
        return count

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        count = 0
        for element in self.store:
            if element is not None:
                count += 1
        
        if count == 0:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        l = []
        for i in self.store:
            if i is not None:
                l.append(i)
        return str(l)



        
