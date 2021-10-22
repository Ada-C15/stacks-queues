
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
        if self.size == self.buffer_size:
            raise QueueFullException
        if self.size == 0:
            self.size += 1
            self.front += 1
            self.rear += 1
            self.store[self.front] = element
            return self.store
        else:
            self.rear = (self.rear + 1) % self.buffer_size
            self.store[self.rear] = element
            self.size += 1
        return self.store

        # # (self.rear + 1) % self.buffer_size
        # """ Adds an element to the Queue
        #     Raises a QueueFullException if all elements
        #     In the store are occupied
        #     returns None
        # """
        #

    def dequeue(self):
        if self.size == 0:
            return QueueEmptyException
        element = self.store[self.front]
        self.store[self.front] = None
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1
        return element

        # """ Removes and returns an element from the Queue
        #     Raises a QueueEmptyException if
        #     The Queue is empty.
        # """
        # #capture element to return in variable
        # pass

    def front(self):
        if self.size == 0:
            return None
        return self.store[self.front]
        # """ Returns an element from the front
        #     of the Queue and None if the Queue
        #     is empty.  Does not remove anything.
        # """

    def size(self):
        # """ Returns the number of elements in
        #     The Queue""

        return self.size

    def empty(self):
        if self.size == 0:
            return True
        else:
            return False

        # """ Returns True if the Queue is empty
        #     And False otherwise.
        # """
        #

    def __str__(self):
        return_list = []
        if self.size == 0:
            return str(return_list)

        current = self.front
        while current != self.rear:
            # print(self.size)
            # for elem in self.store:
            if current is not None:
                return_list.append(self.store[current])
                current = (current + 1) % self.buffer_size

        return_list.append(self.store[self.rear])

        return str(return_list)
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
