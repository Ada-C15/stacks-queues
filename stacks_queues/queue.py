
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

        # if queue is full 
        if self.buffer_size == self.size:
            raise QueueFullException()

        # add to queue
        self.store[self.rear] = element
        # reassign rear ? why? move rear to the next free position
        self.rear = (self.rear + 1) % self.buffer_size
        # increment size by 1 bc of newly added element
        self.size += 1 

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        # if queue is empty 
        if self.size == 0: 
            raise QueueEmptyException()

        # save the element at the front
        element = self.store[self.front]
        # remove the first element by increment the front by 1 
        self.front = (self.front + 1) % self.buffer_size

        # check the front index = the rear index for memory management
        if self.front == self.rear: 
            self.front = 0 
            self.rear = 0 

        # decrement size bc it just lost an element 
        self.size -= 1 

        return element

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
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

        queue_list = []
        for i in range(self.front, self.front + self.size): 
            i = i % self.buffer_size 
            queue_list.append(self.store[i])
        return str(queue_list)
