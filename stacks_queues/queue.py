
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.size == self.buffer_size:
            raise QueueFullException
        
        new_rear = (self.rear + 1) % self.buffer_size
        self.store[new_rear] = element
        self.rear = new_rear
        self.size +=1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException

        previous = self.store[self.front]
        self.store[self.front] = None
        new_front = (self.front + 1) % self.buffer_size
        self.front = new_front
        self.size -= 1

        return previous

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
        return self.store[self.front] == None

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        nums = ""
        for i in range(self.front, self.size + self.front):
            if nums != "":
                nums += ", "
            nums += str(self.store[i%self.buffer_size])
        return f"[{nums}]"

        # for i in range(self.front, self.buffer_size):
        #     if self.store[i] == None:
        #         return f"[{nums}]"
            
        #     if nums != "":
        #         nums += ", "
        #     nums += str(self.store[i])
        
        # for i in range(self.rear+1):
        #     if nums != "":
        #         nums += ", "
        #     nums += str(self.store[i])
        
        # return f"[{nums}]"
