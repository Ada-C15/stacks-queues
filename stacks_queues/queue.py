from typing import ItemsView


INITIAL_QUEUE_SIZE = 20
"""
https://towardsdatascience.com/circular-queue-or-ring-buffer-92c7b0193326
https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
"""
class QueueFullException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        print('calling str')
        if self.message:
            return 'QueueFullException, {0}'.format(self.message)
        else:
            return 'QueueFullException has been raised'
    

class QueueEmptyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        print('calling str')
        if self.message:
            return 'QueueEmptyException, {0}'.format(self.message)
        else:
            return 'QueueEmptyException has been raised'

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
        if ((self.rear +1) % INITIAL_QUEUE_SIZE ==self.front):
            raise QueueFullException('This will break it')

        elif (self.front == -1): 
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
            self.size = self.size + 1
        else:
             
            # next position of rear
            self.rear = (self.rear + 1) % INITIAL_QUEUE_SIZE
            self.store[self.rear] = element
            self.size = self.size + 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty. In the circular Queue it remove the item at the front 
        """
        
        if self.empty():
            raise QueueEmptyException("The Stack is empty")

        # condition for only one element
        elif (self.front == self.rear):
            tmp=self.store[self.front]
            self.front = -1
            self.rear = -1
            self.size -=1
            return tmp

        else:
            tmp = self.store[self.front]
            self.front = (self.front + 1) % INITIAL_QUEUE_SIZE
            self.size -=1
            return tmp

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.size == 0:
            return None
        return self.store[self.front]
        
    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size
        # self if a reference to the current class when in a class method you need to append self to it.  
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
        tmp = []
        if(self.front == -1):
            print ("Queue is Empty")
 
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                tmp.append(self.store[i])
            
 
        else:
            for i in range(self.front, INITIAL_QUEUE_SIZE):
                tmp.append(self.store[i])
            for i in range(0, self.rear + 1):
                tmp.append(self.store[i])
            
 
        if ((self.rear + 1) % INITIAL_QUEUE_SIZE == self.front):
            print("Queue is Full")

        return str(tmp)
        


            
        