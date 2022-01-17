
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        # buffer_size is the capacity of queue
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = -1 
        self.rear = -1
        self.size = 0
    
    def is_full(self):
        """ Method returns a boolean or whether or not the queue is full
        """
        return  self.size == self.buffer_size


    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        # ------------> FIRST METHOD OF IMPLEMENTING ENQUEUE <-----------------
        # if size of queue == to buffer_size/capacity -> raise error
        if self.size == self.buffer_size:
            raise QueueFullException
        
        # if queue is empty -> add to back of queue and incremement size, front and rear
        if self.size == 0:
            self.size += 1
            # self.front: -1 -> 0
            self.front = 0
            # self.rear: -1 -> 0
            self.rear = 0
            # add element to back of queue
            self.store[self.rear] = element
            return self.store
        # if queue is not empty
        else:
            # find the last element -> the end. Add 1 to rear to turn queue into circle 
            self.rear = (self.rear + 1) % self.buffer_size
            self.store[self.rear] = element 

            # need to increment size with addition of new element
            self.size += 1

            return self.store
        
        # ------------> SECOND METHOD OF IMPLEMENTING ENQUEUE <-----------------
        # element is data 

        # if queue is full, raise exception
        # if (self.is_full()):
        #     raise QueueFullException
        
        # self.store[self.rear] = element
        # self.rear = (self.rear + 1) % self.buffer_size
        # self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """

        # ------------> FIRST METHOD OF IMPLEMENTING DEQUEUE <-----------------
        # if queue is empty --> nothing to remove
        if self.size == 0:
            raise QueueEmptyException 
        else:
            # create a temporary variable whose value is the current front of queue
            temp = self.store[self.front]
            # set new value of front of queue to none
            self.store[self.front] = None
            # add 1 to front to turn queue into circle
            self.front = (self.front + 1) % self.buffer_size
            # decrement size of queue
            self.size -= 1
            return temp 

        
        # ------------> SECOND METHOD OF IMPLEMENTING DEQUEUE <-----------------

        # if (self.is_full()):
        #     raise QueueEmptyException
        
        # data = self.store[self.front]
        # self.front = (self.front + 1) % self.buffer_size
        # self.size -= 1

        # return data

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        return self.front
        

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
        list = []
        
        if self.size == 0:
            return list 
        
        current = self.front 

        while current != self.rear:
            if current != None:
                list.append(self.store[current])
                current = (current + 1) % self.buffer_size
        
        list.append(self.store[self.rear])

        return str(list)
