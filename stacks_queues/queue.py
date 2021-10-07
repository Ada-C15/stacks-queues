
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
        #pseudeo code implementation:
        #Move back to the next free position)the next position clockwise
        # back = (back + 1 ) % size;
        #else back = back + 1;

        #You could increment and decrement size if you want to keep track of size

        #check to see if queue is full (front == (back + 1) mod size;)
        if self.front == (self.rear + 1) % self.buffer_size:  #size?
            raise QueueFullException("Queue is full")
        
        #if queue is empty
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element

        else:
        #increment that back pointer
            self.rear = (self.rear + 1) % self.buffer_size;
            self.store[self.rear] = element;

        #why return None?
        return None

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None
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

            #return temp value? why return None here?
            return temp
        
        else:
            temp = self.store[self.front]

            #increment front counter 
            self.front = (self.front + 1) % self.buffer_size

            #return None?
            return temp

        

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        
        # if self.empty:
        #     return None
        
        # else:
        #     temp = self.store[self.front]
        #     #do I need to enqueue this element again?
        #     return temp
        

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
        str = []

        #modulus operater move through the queue (start current index at the front and keep adjusting until i reach the back)
        #maybe use a while
        #prob need to typecaste
        
        for i in range(len(self.store)):
            
            str.append(char)
        
        return str
