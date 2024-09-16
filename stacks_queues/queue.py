
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

        #check to see if queue is full (front == (back + 1) mod size;)
        if self.front == (self.rear + 1) % self.buffer_size:  #size?
            raise QueueFullException("Queue is full")
        
        # # if queue is empty
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element

        else:
        #increment the back pointer
            self.rear = (self.rear + 1) % self.buffer_size
            self.store[self.rear] = element
            self.size += 1

        # return self.rear

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if (self.front == -1):
            raise QueueEmptyException("The Queue is empty")

        
        #if there is only one element in the queue
        elif (self.front == self.rear):
            #store the element in a temp variable
            temp = self.store[self.front]
            #reset front and back pointers to same position/empty queue
            self.front = -1
            self.rear = -1
            return temp
        
        else:
            temp = self.store[self.front]

            #increment front counter 
            self.front = (self.front + 1) % self.buffer_size
            return temp

        

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        
        if (self.front == -1):
            return None

        else:
            return self.store[self.front]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        
        if (self.rear >= self.front):
            size = self.rear - self.front 
        elif (self.front > self.rear):
            size = INITIAL_QUEUE_SIZE - (self.front - self.rear)
        
        return size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if (self.front == self.rear):
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.

        """
        elements = []

        for i in range(self.buffer_size):

            if self.store[self.front] == None:
                return str(elements)
            
            else:

                elements.append(self.store[self.front])
                self.front = (self.front+1) % self.buffer_size
            
            # toStr = [str[element] for element in elements]
        return str(elements)
            




