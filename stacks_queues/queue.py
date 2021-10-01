
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
        if self.size >= self.buffer_size:
            raise QueueFullException()

        self.rear = (self.rear + 1) % self.buffer_size
        self.store[self.rear] = element
        self.size += 1

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if
            The Queue is empty.
            returns None
        """
        if self.empty():
            raise QueueEmptyException()

        self.front = (self.front + 1) % self.buffer_size
        temp_front = self.store[self.front]
        self.store[self.front] = None
        self.size -= 1
        return temp_front

    def get_front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        if self.empty():
            return None
        return self.store[self.front]

    def get_size(self):
        """ Returns the number of elements in
            The Queue
        """
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.get_size() == 0:
            return True
        return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        queue_list = []

        # prints an empty list if the queue is empty
        if self.empty():
            return str(queue_list)

        # if the queue is not empty, append every item from the front pointer to the end of the queue
        for i in range(self.front + 1, self.buffer_size):
            if self.store[i] != None:
                queue_list.append(self.store[i])

        # if the list wraps all the way around, add every item from the beginning of the queue to the rear pointer
        if self.rear <= self.front:

            for i in range(0, self.rear + 1):
                if self.store[i] != None:
                    queue_list.append(self.store[i])

        return str(queue_list)
