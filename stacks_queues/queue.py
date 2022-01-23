INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass # build out?

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

        if ((self.rear + 1) % self.buffer_size == self.front):
            raise QueueFullException()
        elif self.empty():
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
        elif ( (self.rear == self.buffer_size - 1) and (self.front != 0) ):
            self.rear = 0
            self.store[self.rear] = element
        else:
            self.rear += 1
            self.store[self.rear] = element

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """

        if self.empty():
            raise QueueEmptyException()

        content = self.store[self.front]
        self.store[self.front] = None

        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.buffer_size
        return content

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
        return self.__str__().count(",") + 1

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """

        if self.front == -1:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        queue = []
        front = self.front

        while front != self.rear:
            queue.append(self.store[front])
            front += 1
            front %= self.buffer_size

        queue.append(self.store[self.rear])
        return str(queue)
