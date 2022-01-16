
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
        self.rear = 0
        self.size = 0

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        # if self.front == (self.rear + 1) % self.buffer_size:
        if self.size == self.buffer_size:
            raise(QueueFullException)
        if self.rear == self.buffer_size and self.front > 0:
            self.rear = 0
        self.store[self.rear] = element
        self.rear += 1
        self.size += 1
        return None

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.front == self.rear:
            raise(QueueEmptyException)
        temp = self.store[self.front]
        self.store[self.front] = None
        self.front += 1
        self.size -= 1
        return temp

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.front != None:
            return self.front
        return None

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.front == self.rear:
            return True
        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        values = []
        if self.size == 0:
            return None
        for i in range(self.front, self.buffer_size):
            if self.store[i] != None:
                values.append(self.store[i])
        if self.front >= self.rear:
            for j in range(0, self.rear):
                if self.store[j] != None:
                    values.append(self.store[j])

        return str(values)
