
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
      
    # put something in back and comes off through the front
    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        # checks to see if the list is empty
        # if list is empty we want to add the element to the list set it to front
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.store[self.front] = element
        
        elif self.front == (self.rear + 1) % INITIAL_QUEUE_SIZE:
            raise
        
        else:
            self.rear = (self.rear + 1) % INITIAL_QUEUE_SIZE
            self.store[self.rear] = element 
        
        
        
    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
        """
        if self.front == -1 and self.rear == -1:
            return None
        else:
            self.store[self.front + 1] = self.front

    
    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.front == -1 and self.rear == -1: 
            return None
        else:
            return self.store[self.front]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        length = 0
        for position in INITIAL_QUEUE_SIZE:
            if position:
                length += 1
        return length 

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        queue = []
        starting_index = self.store[self.front]
        
        for positions in range(INITIAL_QUEUE_SIZE):
            if self.store[starting_index] == None:
                self.front = (self.rear + 1) % INITIAL_QUEUE_SIZE
            else:
                queue.append(self.store[starting_index])
                self.front = (self.rear + 1) % INITIAL_QUEUE_SIZE
            
        return str(queue)
            
            

            



