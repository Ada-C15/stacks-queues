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
        if self.size == self.buffer_size:
            raise QueueFullException
        if self.size == 0:
            self.size += 1
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
            return self.store
        else:
            self.rear = (self.rear + 1) % self.buffer_size
            self.store[self.rear] = element
            self.size += 1
            return self.store

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if
            The Queue is empty.
            returns None
        """
        if self.size == 0:
            raise QueueEmptyException
        else:
            tmp = self.store[self.front]
            self.store[self.front] = None
            self.front = (self.front + 1) % self.buffer_size
            self.size -= 1
            return tmp

    def front(self):
        return self.front

    def size(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return True

    def __str__(self):
        ordered_list = []
        # other
        # current = self.front
        # for i in range(INITIAL_QUEUE_SIZE):
        #     if self.store[current]:
        #         ordered_list.append(self.store[current])
        #     current = (current + 1) % INITIAL_QUEUE_SIZE
        # return str(ordered_list)

        i = self.front
        while i != self.rear:
            ordered_list.append(self.store[i])
            i = (i + 1) % self.buffer_size
        ordered_list.append(self.store[i])

        return str(ordered_list)
