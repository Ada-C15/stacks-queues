
INITIAL_QUEUE_SIZE = 20

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        # -1 can be None to indicate queue is empty
        self._front = -1
        self.rear = -1
        self.store_size = 0
      

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """

        if (self._front == 0 and self.rear == self.buffer_size - 1) or self.rear == (self._front - 1):
            raise QueueFullException
        # queue is empty
        elif (self._front == -1):
            self.store_size += 1
            self._front = 0
            self.rear = 0
            self.store[self.rear] = element
        # wrap rear
        elif (self.rear == self.buffer_size - 1):
            self.store_size += 1
            self.rear = 0
            self.store[self.rear] = element
        # rear is not at end of list
        else:
            self.store_size += 1
            self.rear = self.rear + 1
            self.store[self.rear] = element
        
        return None   

    def dequeue(self):
        """ Removes an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
            returns None

            Move front pointer and not rear pointer
            Only change rear when queue becomes empty
        """

        # Walkthrough w/Terah:
        # find index of front
        # store value in temp value to return
        # self.store at index of front is going to be None
        # reassign where front is pointing

        # if self.store_size == 0
        if self._front == -1:
            raise QueueEmptyException
        else:
            temp = self.store[self._front]
            self.store[self._front] = None
            self._front = (self._front + 1) % self.buffer_size
            self.store_size -=1
            return temp
        
    
    def front(self):
        """ Returns an element from the front
            of the Queue and None if the Queue
            is empty.  Does not remove anything.
        """
        
        if (self._front == -1):
            return None

        return self.store[0]
        

    def size(self):
        """ Returns the number of elements in
            The Queue
        """
        return len(self.store)

    def empty(self):
        """ Returns True if the Queue is empty
            And False otherwise.
        """
        # ony works if nothing has ever been in queue
        # self._front is only -1 when the queue is first created/initialized
        # if self.store_size == 0:
        if self._front == self.rear+1:
            return True
        else:
            return False

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.

            use mod operator to have current index move through list until rear
            while current_index != self.rear
        """
        queue_list = []
        current = self._front

        while current != self.rear:
            if self.store[current]:
                queue_list.append(self.store[current])
                current = (current + 1) % self.buffer_size
        
        if self.store[current]:
            queue_list.append(self.store[current])

        return str(queue_list)
