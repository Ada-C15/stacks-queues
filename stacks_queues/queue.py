
INITIAL_QUEUE_SIZE = 20
RESIZE_INCREMENT = 5

class QueueFullException(Exception):
    pass

class QueueEmptyException(Exception):
    pass

class Queue:

    def __init__(self):
        self.store = [None] * INITIAL_QUEUE_SIZE
        self.buffer_size = INITIAL_QUEUE_SIZE
        self.front = -1
        self.back = -1
        self.size = 0
        self.resize_increment = RESIZE_INCREMENT
      

    def enqueue(self, element):
        """ Adds an element to the Queue
            Raises a QueueFullException if all elements
            In the store are occupied
            returns None
        """
        if self.size == self.buffer_size:
            self.__enlarge_capacity(self.resize_increment)

        if self.front == -1:
            self.front = 0
            self.back = 0

        self.store[self.back] = element
        self.back = (self.back + 1) % len(self.store)
        self.size += 1


    def dequeue(self):
        """ Removes and returns an element from the Queue
            Raises a QueueEmptyException if 
            The Queue is empty.
        """
        if self.empty():
            raise QueueEmptyException

        element = self.store[self.front]    
        self.front = (self.front + 1) % len(self.store)
        self.size -= 1

        return element
        
        
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
        return self.size == 0

    def __str__(self):
        """ Returns the Queue in String form like:
            [3, 4, 7]
            Starting with the front of the Queue and
            ending with the rear of the Queue.
        """
        return str(self.__get_queue())

    def __enlarge_capacity(self, i):
        queue = self.__get_queue()

        self.store = queue + ([None] * i)
        self.buffer_size += i
        self.front = 0
        self.back = len(queue)
    
    def __get_queue(self):
        queue = []
        if self.front < self.back:
            for i in range(self.front, (self.back) % len(self.store)):
                queue.append(self.store[i])

        if self.back <= self.front:
            for i in range(self.front, len(self.store)):
                queue.append(self.store[i])
            for j in range(self.back):
                queue.append(self.store[j])

        return queue
        


# INITIAL_QUEUE_SIZE = 20

# class QueueFullException(Exception):
#     pass

# class QueueEmptyException(Exception):
#     pass

# class Queue:

#     def __init__(self):
#         self.store = [None] * INITIAL_QUEUE_SIZE
#         self.buffer_size = INITIAL_QUEUE_SIZE
#         self.front = -1
#         self.back = -1
#         self.size = 0
      

#     def enqueue(self, element):
#         """ Adds an element to the Queue
#             Raises a QueueFullException if all elements
#             In the store are occupied
#             returns None
#         """
#         if self.size == self.buffer_size:
#             raise QueueFullException

#         if self.front == -1:
#             self.front = 0
#             self.back = 0

#         self.store[self.back] = element
#         self.back = (self.back + 1) % len(self.store)
#         self.size += 1


#     def dequeue(self):
#         """ Removes and returns an element from the Queue
#             Raises a QueueEmptyException if 
#             The Queue is empty.
#         """
#         if self.empty():
#             raise QueueEmptyException

#         element = self.store[self.front]    
#         self.front = (self.front + 1) % len(self.store)
#         self.size -= 1

#         return element
        
        
#     def front(self):
#         """ Returns an element from the front
#             of the Queue and None if the Queue
#             is empty.  Does not remove anything.
#         """
#         if self.empty():
#             return None

#         return self.store[self.front]
        

#     def size(self):
#         """ Returns the number of elements in
#             The Queue
#         """
#         return self.size

#     def empty(self):
#         """ Returns True if the Queue is empty
#             And False otherwise.
#         """
#         return self.size == 0

#     def __str__(self):
#         """ Returns the Queue in String form like:
#             [3, 4, 7]
#             Starting with the front of the Queue and
#             ending with the rear of the Queue.
#         """
#         queue = []
#         if self.front < self.back:
#             for i in range(self.front, (self.back) % len(self.store)):
#                 queue.append(self.store[i])

#         if self.back <= self.front:
#             for i in range(self.front, len(self.store)):
#                 queue.append(self.store[i])
#             for j in range(self.back):
#                 queue.append(self.store[j])
#         return str(queue)