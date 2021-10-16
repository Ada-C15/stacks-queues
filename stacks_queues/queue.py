
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE 
        # how many can I fit in circular buffer
        self.buffer_size = INITIAL_QUEUE_SIZE
        # initial pointer to start of queue (not within 0-19 indexes)
        self.front = -1
        # initial pointer to start of queue (not within 0-19 indexes)
        self.rear = -1
        # How many elements are already in the cb - initially zero 
        self.size = 0
    
    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """

        # Queue is full
        if self.size >= self.buffer_size:  # 0 > 20 ? 
            raise QueueFullException("Queue is Full")

        # if rear pointer is past the allowed size, cannot insert anymore, reset it 
        if self.rear >= (self.buffer_size - 1):   # -1 >= 19 ? index
            #reset rear
            self.rear = -1

        # after checking queue is not full and there's still space in queue we
        # can insert it and need to move rear and update size to keep track 
        
        self.store[self.rear + 1] = element  # self.store[0] = element
        # keep track of how many elements in array
        self.size += 1
        self.rear += 1

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
        """
        # check queue is not empty and then just if not empty, dequeue and update pointers and size
        if self.empty():
            raise QueueEmptyException("Queue is empty")

        if self.front >= (self.buffer_size - 1):   # -1 >= 19 ? index
            #reset rear
            self.front = -1

        # not empty, just dequeue, update front pointer and size
        if self.store[self.front+1]:
            dequeued = self.store[self.front+1]
            self.front += 1
            self.size -= 1 
            return dequeued

        # self.store = [1, 2, 3] 
        # self.buffer_size = 20
        # self.front = 0
        # self.rear = -1
        # self.size = 3

        # if self.store[self.front]:
        #     dequeued = self.store[self.front]
        #     self.front += 1
        #     self.size -= 1 
        #     return dequeued    
        
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
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.empty():
            return self.store
        else:
            return f'{[elem for elem in self.store if elem]}'


        
