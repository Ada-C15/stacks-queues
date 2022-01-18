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
        if self.size == self.buffer_size:
            raise QueueFullException("i'm full 🤰")
        else:
            self.size += 1
            self.store[self.rear] = element
            self.rear = (self.rear + 1) % self.buffer_size


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if
            The Queue is empty.
        """

        if self.empty():
            raise QueueEmptyException("i'm empty")
        else:
            temp = self._front()
            self.size -= 1
            self.front = (self.front + 1) % self.buffer_size
            return temp

    def _front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        return self.store[self.front] if not self.empty() else None

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        f = self.front
        helper_list = []

        for i in range(self.size):
            helper_list.append(self.store[(f+i) % self.buffer_size])

        return "["+", ".join(list(map(str, helper_list)))+"]"