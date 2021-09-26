
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
        if (self.rear + 1) % self.buffer_size == self.front:
            #The Queue is full
            raise QueueFullException("Queue is full")
        elif self.front == -1:
            # Queue is empty
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
            self.size += 1
        else:
            self.rear = (self.rear +1) % self.buffer_size
            # rear needs to wrap around
            self.store[self.rear] = element
            self.size += 1
        
    

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
        """
        if self.front == -1:
            #queue is empty
            raise QueueEmptyException("Queue is empty")
        
        
        data = self.store[self.front]
        #override the element being deleted
        self.store[self.front] = None
        self.size -= 1
        
        #if the queue is empty
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.buffer_size -1:
            
            self.front = 0
        else:
            self.front += 1
        
        return data

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
        if self.size == 0:
            return True
    
        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        data = []
        
        if self.front == -1:
            return str(data)
        elif self.front <= self.rear:
            for i in range(self.front, (self.rear+1)):
                data.append(self.store[i])
        else:
            for i in range(self.front, self.buffer_size):
                data.append(self.store[i])
            for i in range(0, self.rear +1):
                data.append(self.store[i])
        return str(data)
