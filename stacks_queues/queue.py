
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
            raise QueueFullException()


        self.rear = (self.rear + 1) % self.buffer_size
        self.store[self.rear] = element
        self.size += 1


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException()

        return_value = self.store[self.front]
        self.store[self.front] = None
        self.front += 1
        self.size -= 1
        return return_value
        

    def get_front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """

        pass
        

    def find_size(self):
        """ Returns the number of elements in
            The Queue
        """
        pass

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.size <= 0:
            return True
        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """

        if self.rear < self.front:
            items_str = ", ".join(str(self.store[item]) for item in range(self.front, self.size - 1))
            second_set_items = ", ".join(str(self.store[item]) for item in range(-1, self.rear + 1))
            joined_items = "[" + items_str + ", " + second_set_items + "]"
            return joined_items
        
        else:
            items_str = ", ".join(str(self.store[item]) for item in range(self.front, self.rear + 1))
            joined_items = "[" + items_str + "]"
            return joined_items