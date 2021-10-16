
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE 
        self.buffer_size = INITIAL_QUEUE_SIZE
        # pointers
        self.front = -1
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
        if self.size >= self.buffer_size:  
            raise QueueFullException("Queue is Full")

        # if rear pointer is past the allowed size, cannot insert anymore, reset it 
        if self.rear >= (self.buffer_size - 1):   # index, not size
            #reset rear
            self.rear = -1

        # after checking queue is not full & there's space in queue we
        # can insert it and need to move rear and update size to keep track 
        self.store[self.rear + 1] = element 
        # keep track of how many elements in array / where end of queue is
        self.size += 1
        self.rear += 1

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
        """
        if self.empty():
            raise QueueEmptyException("Queue is empty")

        if self.front >= (self.buffer_size - 1):  
            self.front = -1

        # not empty?, just dequeue, update front pointer and size  
        if self.store[self.front + 1]:
            dequeued = self.store[self.front + 1]
            self.front += 1
            self.size -= 1 
            return dequeued
        
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
        # return string of empty array
        if self.empty():
            return f'{self.store}'
        
        # will append to this arr, just what's not none in the correct order
        str_queue = []
        # temporary pointer so self.front doesn't actually move
        front = self.front + 1
        # front has made it past the end of the list
        if front >= len(self.store):
            # reset temp index it to start at the front of array
            front = 0

        # front hasn't caught up with rear
        while front != self.rear:
            str_queue.append(self.store[front])
            # update pointer after appending
            front += 1

            if front >= (self.buffer_size):   
                #reset to start of the loop
                front = 0
        #rear because before last element they are the same, 
        # could do self.store[rear] bc we are really appending the last one
        str_queue.append(self.store[front])
        
        return f'{str_queue}'
        

        
