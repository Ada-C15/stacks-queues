
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
        # if the size of the queue equals the size of the buffer, the queue is full
        if self.size == self.buffer_size:
            raise QueueFullException()
        # if the queue is empty, move the front pointer to the next index position (0)
        if self.front == -1:
            self.front = 0
        
        # reassign the rear pointer to the remainder of: the next index position of rear divided by the buffer size
        # (self.rear + 1) / buffer size
        # aka move to the next index position
        self.rear = (self.rear + 1) % self.buffer_size
        # insert element at the back of the array
        self.store[self.rear] = element
        # increment queue size by 1
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.size == 0:
            raise QueueEmptyException()

        element = self.store[self.front]
        self.store[self.front] = None

        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1
        return element

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None

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
        temp_arr = []

        temp_front = self.front

        if self.size == 0:
            return "[]"

        while temp_front != self.rear:
            temp_arr.append(self.store[temp_front])
            temp_front = (temp_front + 1) % self.buffer_size
        
        temp_arr.append(self.store[temp_front])

        return str(temp_arr)

        # for i in range(self.front, self.front + self.size):
        #     i = i % self.buffer_size
        #     queue.append(self.store[i])