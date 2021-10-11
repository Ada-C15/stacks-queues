
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
        if (self.front == 0 and self.rear == self.buffer_size - 1) or (self.rear == (self.front-1) % (self.buffer_size-1)):
            raise QueueFullException("Queue is full.")
        elif self.empty():
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
        elif (self.rear == self.buffer_size - 1 and self.front != 0):
            self.rear = 0
            self.store[self.rear] = element
        else:
            self.rear += 1
            self.store[self.rear] = element

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if
            The Queue is empty.
            returns None
        """
        if self.empty():
            raise QueueEmptyException('Queue is empty.')

        data = self.store[self.front]
        self.store[self.front] = None

        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.front == self.buffer_size-1):
            self.front = 0
        else:
            self.front += 1
        return data

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
        size = self.__str__().count(",") + 1
        return size

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
        if self.empty():
            return "[]"

        q = []
        front = self.front
        while front != self.rear:
            q.append(self.store[front])
            front += 1
            front %= self.buffer_size
        q.append(self.store[self.rear])
        return str(q)
