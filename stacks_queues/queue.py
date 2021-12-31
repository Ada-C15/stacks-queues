
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
        # buffer is full
        if self.size == self.buffer_size:
            raise QueueFullException

        """
          f
        0 1 2 3 4
        - b c - -
            r
        size = 1
        buffer_size = 5

        enqueue(a)
        enqueue(b)
        enqueue(c)
        dequeue() -> a
        """

        # initialiaze buffer, because it is new
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.store[self.rear] = element
            self.size += 1
            return

        self.rear = (self.rear + 1) % self.buffer_size
        self.store[self.rear] = element
        self.size += 1

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException
        
        dequeued_element_value = self.store[self.front] if not self.empty() else None

        # TODO: explore why this does not work to pass the tests
        # dequeued_element_value = self.front()

        self.store[self.front] = None
        self.front = (self.front + 1) % self.buffer_size
        self.size -= 1

        return dequeued_element_value

    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if not self.empty():
            return self.store[self.front]
        else: 
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
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        result = []
        for index in range(self.front, self.front + self.size):
            index = index % self.buffer_size
            result.append(self.store[index])
        return str(result)