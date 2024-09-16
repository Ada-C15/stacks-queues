
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
        if self.full():
            raise QueueFullException("The queue is full")
        elif self.empty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1)%self.buffer_size
        self.store[self.rear] = element
        self.size += 1 
        return None

    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException("The queue is empty")
        data = self.store[self.front]
        self.store[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1)%self.buffer_size
            self.size -= 1  
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
        return self.size

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False

    def full(self):
        """ Returns True if the Queue is full
            And False otherwise.
        """
        if (self.rear + 1) %  self.buffer_size == self.front:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        if self.full():
            my_list = []
            for i in self.store[self.front:]:
                if i == None:
                    break
                my_list.append(i)

            for i in self.store[:self.rear+1]:
                if i == None:
                    break
                my_list.append(i)

            return str(my_list)
        else:
            new_list = self.store[self.front:self.rear+1]
            return str(new_list)
